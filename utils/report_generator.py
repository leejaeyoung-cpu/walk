import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import os
import zipfile
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
try:
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
except:
    pass
plt.rcParams['axes.unicode_minus'] = False

DB_FILE = "church_plan.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def generate_dept_report(dept_name, year, save_dir):
    print(f"Processing: {dept_name}")
    conn = get_connection()
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
    
    try:
        # 데이터 전처리 (타입 변환 및 결측치 처리)
        df['month'] = pd.to_numeric(df['month'], errors='coerce').fillna(0).astype(int)
        df['church_subsidy'] = pd.to_numeric(df['church_subsidy'], errors='coerce').fillna(0)
        df['self_funded'] = pd.to_numeric(df['self_funded'], errors='coerce').fillna(0)
        df['total'] = pd.to_numeric(df['total'], errors='coerce').fillna(0)

        # 캔버스 설정 (A4 크기)
        fig = plt.figure(figsize=(11.69, 16.53)) 
        
        # 1. 제목 (상단 고정)
        # 제목 폰트 크기 자동 조절
        title_fontsize = 28 if len(dept_name) < 10 else 24
        fig.text(0.5, 0.96, f"{year}년 {dept_name} 사업계획 보고서", 
                 ha='center', va='top', fontsize=title_fontsize, fontweight='bold')

        # 2. 예산 요약 표 (상단 영역: y=0.55 ~ 0.90)
        # add_axes([left, bottom, width, height])
        ax_table = fig.add_axes([0.1, 0.55, 0.8, 0.35])
        ax_table.axis('off')
        
        table_df = df.copy()
        table_df.columns = ['월', '사업내용', '본당보조', '자체', '계']
        table_df['월'] = table_df['월'].apply(lambda x: f"{x}월" if x > 0 else '-')
        for col in ['본당보조', '자체', '계']:
            table_df[col] = table_df[col].apply(lambda x: f"{x:,.0f}")

        table = ax_table.table(
            cellText=table_df.values,
            colLabels=table_df.columns,
            cellLoc='center',
            loc='center',
            colColours=['#e6f2ff']*len(table_df.columns)
        )
        # 표 높이/폰트 조정 (데이터 양에 따라 자동 조절되지만 영역은 고정)
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        # 행 높이 계산: 영역 높이 / (행 개수 + 헤더)
        # 너무 작아지지 않게 최소 높이 보장 로직은 생략하고, 기본 스케일 사용
        table.scale(1, 1.5)

        # 3. 파이 차트 (하단 좌측 영역: y=0.15 ~ 0.45, x=0.05 ~ 0.45)
        ax_pie = fig.add_axes([0.05, 0.15, 0.4, 0.3])
        pie_data = df.groupby('event_name')['total'].sum().sort_values(ascending=False)
        
        if not pie_data.empty and pie_data.sum() > 0:
            # 상위 5개 + 기타
            if len(pie_data) > 6:
                top_5 = pie_data.iloc[:5]
                others_sum = pie_data.iloc[5:].sum()
                others = pd.Series([others_sum], index=['기타'])
                pie_data = pd.concat([top_5, others])
            
            total_sum = pie_data.sum()
            labels_with_pct = [f"{name} ({val/total_sum*100:.1f}%)" for name, val in zip(pie_data.index, pie_data.values)]
            
            colors = plt.cm.Set3.colors
            wedges, texts = ax_pie.pie(
                pie_data, 
                startangle=90, 
                colors=colors,
                labels=None
            )
            centre_circle = plt.Circle((0,0),0.70,fc='white')
            ax_pie.add_artist(centre_circle)
            ax_pie.set_title("사업별 예산 비중", fontsize=16, fontweight='bold', pad=20)
            
            # 범례 (파이 차트 아래쪽 공간 활용)
            ax_pie.legend(
                wedges, 
                labels_with_pct, 
                title="사업명 (비중)", 
                loc="upper center", 
                bbox_to_anchor=(0.5, -0.05), # 차트 바로 아래
                fontsize='small',
                ncol=1 # 한 줄로 길게
            )
        else:
            ax_pie.text(0.5, 0.5, "데이터 없음", ha='center', va='center')
            ax_pie.axis('off')

        # 4. 막대 차트 (하단 우측 영역: y=0.15 ~ 0.45, x=0.55 ~ 0.95)
        ax_bar = fig.add_axes([0.55, 0.15, 0.4, 0.3])
        
        valid_monthly_df = df[df['month'] > 0]
        if not valid_monthly_df.empty:
            monthly_subsidy = valid_monthly_df.groupby('month')['church_subsidy'].sum()
            monthly_self = valid_monthly_df.groupby('month')['self_funded'].sum()
            months = monthly_subsidy.index
            
            ax_bar.bar(months, monthly_subsidy, color='#ff9999', alpha=0.9, label='본당보조')
            ax_bar.bar(months, monthly_self, bottom=monthly_subsidy, color='#66b3ff', alpha=0.9, label='자체')
            
            ax_bar.set_title("월별 지출 계획 (재원별)", fontsize=16, fontweight='bold', pad=20)
            ax_bar.set_xlabel("월")
            ax_bar.set_ylabel("금액 (천원)")
            ax_bar.set_xticks(months)
            ax_bar.grid(axis='y', linestyle='--', alpha=0.5)
            ax_bar.legend(loc='upper right')
            
            # 값 표시 (너무 겹치면 생략 가능하지만 일단 유지)
            for i, month in enumerate(months):
                total = monthly_subsidy.get(month, 0) + monthly_self.get(month, 0)
                if total > 0:
                    ax_bar.text(month, total, f'{int(total):,}', ha='center', va='bottom', fontsize=8)
        else:
            ax_bar.text(0.5, 0.5, "월별 데이터 없음", ha='center', va='center')
            ax_bar.axis('off')

        # 5. 총계 요약 (최하단 영역: y=0.02 ~ 0.12)
        ax_summary = fig.add_axes([0.1, 0.02, 0.8, 0.1])
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

        save_path = os.path.join(save_dir, f"{dept_name}_{year}_report.png")
        
        # tight_layout 제거 (절대 좌표 사용하므로 불필요)
        plt.savefig(save_path, dpi=150) # bbox_inches='tight' 제거 (고정 크기 유지)
        plt.close()
        return True

    except Exception as e:
        print(f"❌ {dept_name} 보고서 생성 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

def generate_all_reports_zip(year=2026):
    # 저장 디렉토리 설정
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reports_dir = os.path.join(base_dir, "reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        
    # 모든 단체 조회
    conn = get_connection()
    depts = pd.read_sql("SELECT name FROM departments", conn)
    conn.close()
    
    generated_files = []
    
    # 보고서 생성
    for dept_name in depts['name']:
        if generate_dept_report(dept_name, year, reports_dir):
            generated_files.append(f"{dept_name}_{year}_report.png")
            
    # ZIP 압축
    zip_path = os.path.join(reports_dir, f"church_reports_{year}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in generated_files:
            file_path = os.path.join(reports_dir, file)
            zipf.write(file_path, file)
            
    return zip_path
