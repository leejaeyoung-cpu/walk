import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import os
from matplotlib import font_manager, rc

# 한글 폰트 설정 (Windows)
font_path = "C:/Windows/Fonts/malgun.ttf"
try:
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
except:
    print("⚠️ 맑은 고딕 폰트를 찾을 수 없습니다. 기본 폰트를 사용합니다.")

plt.rcParams['axes.unicode_minus'] = False

# DB 연결 및 데이터 조회
def get_data(dept_name, year=2026):
    # 상위 디렉토리의 DB 파일 경로
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "church_plan.db")
    conn = sqlite3.connect(db_path)
    
    query = """
        SELECT b.month, b.event_name, b.church_subsidy, b.self_funded, b.total
        FROM budgets b
        JOIN annual_plans ap ON b.annual_plan_id = ap.id
        JOIN departments d ON ap.department_id = d.id
        WHERE d.name = ? AND ap.year = ?
        ORDER BY b.month, b.day
    """
    df = pd.read_sql(query, conn, params=(dept_name, year))
    conn.close()
    return df

def create_report(dept_name):
    df = get_data(dept_name)
    
    if df.empty:
        print(f"❌ {dept_name} 데이터가 없습니다.")
        return

    # 캔버스 설정 (A4 비율, 고해상도)
    fig = plt.figure(figsize=(11.69, 16.53)) 
    fig.suptitle(f"2026년 {dept_name} 사업계획 보고서", fontsize=28, fontweight='bold', y=0.96)

    # 그리드 레이아웃 설정 (4행 2열)
    # 1. 예산 요약 표 (상단 절반 차지)
    ax_table = plt.subplot2grid((4, 2), (0, 0), colspan=2, rowspan=2)
    ax_table.axis('off')
    
    # 테이블 데이터 준비
    table_df = df.copy()
    table_df.columns = ['월', '사업내용', '본당보조', '자체', '계']
    table_df['월'] = table_df['월'].fillna('-').astype(str).apply(lambda x: x.replace('.0', '') + '월' if x != '-' else '-')
    
    # 천원 단위 콤마 추가
    for col in ['본당보조', '자체', '계']:
        table_df[col] = table_df[col].apply(lambda x: f"{x:,.0f}")

    # 테이블 그리기
    table = ax_table.table(
        cellText=table_df.values,
        colLabels=table_df.columns,
        cellLoc='center',
        loc='center',
        colColours=['#e6f2ff']*len(table_df.columns)
    )
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.8) # 높이 조절

    # 2. 파이 차트 (중단 좌측) - 사업별 비중
    ax_pie = plt.subplot2grid((4, 2), (2, 0))
    pie_data = df.groupby('event_name')['total'].sum().sort_values(ascending=False)
    
    # 색상 팔레트
    colors = plt.cm.Set3.colors
    
    wedges, texts, autotexts = ax_pie.pie(
        pie_data, 
        labels=None, # 라벨이 겹칠 수 있어 범례로 대체하거나 생략
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors,
        pctdistance=0.85
    )
    # 도넛 차트 스타일
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    ax_pie.add_artist(centre_circle)
    
    ax_pie.set_title("사업별 예산 비중", fontsize=16, fontweight='bold')
    ax_pie.legend(wedges, pie_data.index, title="사업명", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # 3. 막대 차트 (중단 우측) - 월별 지출 (누적 막대: 본당 vs 자체)
    ax_bar = plt.subplot2grid((4, 2), (2, 1))
    
    # 월별 데이터 집계
    monthly_subsidy = df.groupby('month')['church_subsidy'].sum()
    monthly_self = df.groupby('month')['self_funded'].sum()
    months = monthly_subsidy.index
    
    # 누적 막대 그리기
    p1 = ax_bar.bar(months, monthly_subsidy, color='#ff9999', alpha=0.9, label='본당보조')
    p2 = ax_bar.bar(months, monthly_self, bottom=monthly_subsidy, color='#66b3ff', alpha=0.9, label='자체')
    
    ax_bar.set_title("월별 지출 계획 (재원별)", fontsize=16, fontweight='bold')
    ax_bar.set_xlabel("월")
    ax_bar.set_ylabel("금액 (천원)")
    ax_bar.set_xticks(months)
    ax_bar.grid(axis='y', linestyle='--', alpha=0.5)
    ax_bar.legend(loc='upper right')
    
    # 막대 위에 총액 표시
    for i, month in enumerate(months):
        total = monthly_subsidy[month] + monthly_self[month]
        if total > 0:
            ax_bar.text(month, total, f'{int(total):,}', ha='center', va='bottom', fontsize=9)

    # 4. 총계 요약 (하단)
    ax_summary = plt.subplot2grid((4, 2), (3, 0), colspan=2)
    ax_summary.axis('off')
    
    total_budget = df['total'].sum()
    total_subsidy = df['church_subsidy'].sum()
    total_self = df['self_funded'].sum()
    
    summary_text = (
        f"총 예산 합계: {total_budget:,.0f} 천원\n\n"
        f"──────────────\n\n"
        f"본당 지원금: {total_subsidy:,.0f} 천원   |   자체 조달금: {total_self:,.0f} 천원"
    )
    
    ax_summary.text(0.5, 0.5, summary_text, ha='center', va='center', fontsize=20, fontweight='bold',
                    bbox=dict(facecolor='#f8f9fa', edgecolor='#2c3e50', boxstyle='round,pad=2', linewidth=2))

    # 저장
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    save_path = os.path.join(reports_dir, f"{dept_name}_2026_report.png")
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(save_path, dpi=150, bbox_inches='tight') # dpi 150 for reasonable file size
    print(f"✅ 보고서 생성 완료: {save_path}")
    plt.close()

if __name__ == "__main__":
    create_report("어린이복사단")
