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
    
    if df.empty:
        return False

    # 캔버스 설정
    fig = plt.figure(figsize=(11.69, 16.53)) 
    fig.suptitle(f"{year}년 {dept_name} 사업계획 보고서", fontsize=28, fontweight='bold', y=0.96)

    # 1. 예산 요약 표
    ax_table = plt.subplot2grid((4, 2), (0, 0), colspan=2, rowspan=2)
    ax_table.axis('off')
    
    table_df = df.copy()
    table_df.columns = ['월', '사업내용', '본당보조', '자체', '계']
    table_df['월'] = table_df['월'].fillna('-').astype(str).apply(lambda x: x.replace('.0', '') + '월' if x != '-' else '-')
    
    for col in ['본당보조', '자체', '계']:
        table_df[col] = table_df[col].apply(lambda x: f"{x:,.0f}")

    table = ax_table.table(
        cellText=table_df.values,
        colLabels=table_df.columns,
        cellLoc='center',
        loc='center',
        colColours=['#e6f2ff']*len(table_df.columns)
    )
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.8)

    # 2. 파이 차트 (사업별 비중)
    ax_pie = plt.subplot2grid((4, 2), (2, 0))
    pie_data = df.groupby('event_name')['total'].sum().sort_values(ascending=False)
    colors = plt.cm.Set3.colors
    
    wedges, texts, autotexts = ax_pie.pie(
        pie_data, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85
    )
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    ax_pie.add_artist(centre_circle)
    ax_pie.set_title("사업별 예산 비중", fontsize=16, fontweight='bold')
    ax_pie.legend(wedges, pie_data.index, title="사업명", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # 3. 누적 막대 차트 (월별 지출)
    ax_bar = plt.subplot2grid((4, 2), (2, 1))
    monthly_subsidy = df.groupby('month')['church_subsidy'].sum()
    monthly_self = df.groupby('month')['self_funded'].sum()
    months = monthly_subsidy.index
    
    ax_bar.bar(months, monthly_subsidy, color='#ff9999', alpha=0.9, label='본당보조')
    ax_bar.bar(months, monthly_self, bottom=monthly_subsidy, color='#66b3ff', alpha=0.9, label='자체')
    
    ax_bar.set_title("월별 지출 계획 (재원별)", fontsize=16, fontweight='bold')
    ax_bar.set_xlabel("월")
    ax_bar.set_ylabel("금액 (천원)")
    ax_bar.set_xticks(months)
    ax_bar.grid(axis='y', linestyle='--', alpha=0.5)
    ax_bar.legend(loc='upper right')
    
    for i, month in enumerate(months):
        total = monthly_subsidy[month] + monthly_self[month]
        if total > 0:
            ax_bar.text(month, total, f'{int(total):,}', ha='center', va='bottom', fontsize=9)

    # 4. 총계 요약
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

    save_path = os.path.join(save_dir, f"{dept_name}_{year}_report.png")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    return True

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
