import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# ME 생성 또는 가져오기
dept_id = create_department("ME")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == 'ME']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장', 'name': '한상만', 'baptismal_name': '아만도', 'contact': '', 'region': ''},
    {'position': '단장', 'name': '김은주', 'baptismal_name': '아네스', 'contact': '', 'region': ''}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '교구 신년미사 참석', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '워크샵', 'church_subsidy': 50, 'self_funded': 0, 'total': 50},
    {'month': 9, 'day': None, 'weekday': '', 'event_name': 'MR 부부피정', 'church_subsidy': 0, 'self_funded': 40, 'total': 40},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '남동지구 ME 가족모임', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '주말 체험 교육', 'church_subsidy': 0, 'self_funded': 60, 'total': 60}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: ME")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
