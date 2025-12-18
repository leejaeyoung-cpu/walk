import sqlite3
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "church_plan.db")

def get_connection():
    """데이터베이스 연결 반환"""
    return sqlite3.connect(DB_FILE)

# ========== 단체 관련 함수 ==========

def get_all_departments():
    """모든 단체 조회"""
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM departments ORDER BY name", conn)
    conn.close()
    return df

def create_department(name):
    """단체 생성"""
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO departments (name) VALUES (?)", (name,))
        conn.commit()
        dept_id = c.lastrowid
        conn.close()
        return dept_id
    except sqlite3.IntegrityError:
        conn.close()
        return None

# ========== 연간 계획 관련 함수 ==========

def get_or_create_annual_plan(dept_id, year):
    """연간 계획 조회 또는 생성"""
    conn = get_connection()
    c = conn.cursor()
    
    c.execute("SELECT id FROM annual_plans WHERE department_id = ? AND year = ?", (dept_id, year))
    result = c.fetchone()
    
    if result:
        plan_id = result[0]
    else:
        c.execute("INSERT INTO annual_plans (department_id, year) VALUES (?, ?)", (dept_id, year))
        conn.commit()
        plan_id = c.lastrowid
    
    conn.close()
    return plan_id

# ========== 회원 관련 함수 ==========

def get_members(plan_id):
    """특정 계획의 회원 조회"""
    conn = get_connection()
    df = pd.read_sql(
        "SELECT position, name, baptismal_name, contact, region FROM members WHERE annual_plan_id = ? ORDER BY id",
        conn,
        params=(plan_id,)
    )
    conn.close()
    return df

def save_members(plan_id, members_data):
    """회원 데이터 저장 (기존 데이터 삭제 후 저장)"""
    conn = get_connection()
    c = conn.cursor()
    
    # 기존 데이터 삭제
    c.execute("DELETE FROM members WHERE annual_plan_id = ?", (plan_id,))
    
    # 새 데이터 삽입
    for member in members_data:
        c.execute("""
            INSERT INTO members (annual_plan_id, position, name, baptismal_name, contact, region)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            plan_id,
            member.get('position', ''),
            member.get('name', ''),
            member.get('baptismal_name', ''),
            member.get('contact', ''),
            member.get('region', '')
        ))
    
def update_members_from_df(plan_id, df):
    """데이터프레임 내용을 바탕으로 회원 명단 업데이트 (기존 삭제 후 재등록)"""
    conn = get_connection()
    c = conn.cursor()
    
    try:
        # 기존 명단 삭제
        c.execute("DELETE FROM members WHERE annual_plan_id = ?", (plan_id,))
        
        # 새 명단 등록
        for _, row in df.iterrows():
            c.execute("""
                INSERT INTO members (annual_plan_id, position, name, baptismal_name, contact, region) 
                VALUES (?, ?, ?, ?, ?, ?)""", 
                (
                    plan_id,
                    row['직책'],
                    row['성명'],
                    row['세례명'],
                    row['연락처'],
                    row['구역']
                ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating members: {e}")
        return False
    finally:
        conn.close()

def update_budgets_from_df(plan_id, df):
    """데이터프레임 내용을 바탕으로 예산안 업데이트 (기존 삭제 후 재등록)"""
    conn = get_connection()
    c = conn.cursor()
    
    try:
        # 기존 예산 삭제
        c.execute("DELETE FROM budgets WHERE annual_plan_id = ?", (plan_id,))
        
        # 새 예산 등록
        for _, row in df.iterrows():
            # 금액에서 콤마 제거 및 정수 변환 안전 처리
            def clean_money(val):
                if isinstance(val, str):
                    return int(val.replace(',', '').replace('원', ''))
                return int(val) if val else 0

            # 월/일 처리
            month = int(row['월']) if row['월'] and row['월'] != '' else None
            day = int(row['일']) if row['일'] and row['일'] != '' else None

            c.execute("""
                INSERT INTO budgets (annual_plan_id, month, day, weekday, event_name, church_subsidy, self_funded, total) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
                (
                    plan_id,
                    month,
                    day,
                    row['요일'],
                    row['사업내용'],
                    clean_money(row['본당보조']),
                    clean_money(row['자체']),
                    clean_money(row['계'])
                ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating budgets: {e}")
        return False
    finally:
        conn.close()


# ========== 예산 관련 함수 ==========

def get_budgets(plan_id):
    """특정 계획의 예산 조회"""
    conn = get_connection()
    df = pd.read_sql(
        "SELECT month, day, weekday, event_name, church_subsidy, self_funded, total FROM budgets WHERE annual_plan_id = ? ORDER BY month, day",
        conn,
        params=(plan_id,)
    )
    conn.close()
    return df

def save_budgets(plan_id, budgets_data):
    """예산 데이터 저장 (기존 데이터 삭제 후 저장)"""
    conn = get_connection()
    c = conn.cursor()
    
    # 기존 데이터 삭제
    c.execute("DELETE FROM budgets WHERE annual_plan_id = ?", (plan_id,))
    
    # 새 데이터 삽입
    for budget in budgets_data:
        c.execute("""
            INSERT INTO budgets (annual_plan_id, month, day, weekday, event_name, church_subsidy, self_funded, total)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            plan_id,
            budget.get('month'),
            budget.get('day'),
            budget.get('weekday', ''),
            budget.get('event_name', ''),
            budget.get('church_subsidy', 0),
            budget.get('self_funded', 0),
            budget.get('total', 0)
        ))
    
    conn.commit()
    conn.close()
    return len(budgets_data)

def get_all_budgets_by_year(year):
    """특정 년도의 모든 단체 예산 조회 (시각화용)"""
    conn = get_connection()
    query = """
        SELECT d.name as department, b.month, b.event_name, 
               b.church_subsidy, b.self_funded, b.total
        FROM budgets b
        JOIN annual_plans ap ON b.annual_plan_id = ap.id
        JOIN departments d ON ap.department_id = d.id
        WHERE ap.year = ?
        ORDER BY d.name, b.month, b.day
    """
    df = pd.read_sql(query, conn, params=(year,))
    conn.close()
    return df

def get_budget_summary_by_department(year):
    """단체별 예산 요약"""
    conn = get_connection()
    query = """
        SELECT d.name as department,
               SUM(b.church_subsidy) as total_church_subsidy,
               SUM(b.self_funded) as total_self_funded,
               SUM(b.total) as total_budget
        FROM budgets b
        JOIN annual_plans ap ON b.annual_plan_id = ap.id
        JOIN departments d ON ap.department_id = d.id
        WHERE ap.year = ?
        GROUP BY d.name
        ORDER BY total_budget DESC
    """
    df = pd.read_sql(query, conn, params=(year,))
    conn.close()
    return df
