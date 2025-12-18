import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import get_all_departments, get_or_create_annual_plan
import sqlite3

# 독서단 ID 가져오기
depts = get_all_departments()
dept_id = int(depts[depts['name'] == '독서단']['id'].values[0])

# 연간 계획 ID 가져오기
plan_id = get_or_create_annual_plan(dept_id, 2026)

print(f"독서단 (plan_id: {plan_id})의 예산 내역을 삭제합니다...")

# 데이터베이스 연결
from database.db_utils import get_connection
conn = get_connection()
c = conn.cursor()

# 예산 삭제
c.execute("DELETE FROM budgets WHERE annual_plan_id = ?", (plan_id,))
deleted_count = c.rowcount

conn.commit()
conn.close()

print(f"✅ {deleted_count}건의 예산 내역이 삭제되었습니다.")
