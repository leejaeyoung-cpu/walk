import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 반주단 생성 또는 가져오기
dept_id = create_department("반주단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '반주단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '반주단장', 'name': '정주희', 'baptismal_name': '마틸다', 'contact': '010-2325-4735', 'region': '에코12'},
    {'position': '단원', 'name': '이세현', 'baptismal_name': '비아', 'contact': '010-2839-0270', 'region': '풍림'},
    {'position': '단원', 'name': '임수진', 'baptismal_name': '헬레나', 'contact': '010-9498-3861', 'region': '에코11'},
    {'position': '단원', 'name': '강선희', 'baptismal_name': '세실리아', 'contact': '010-9281-7413', 'region': '신일 해피트리'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': None, 'day': None, 'weekday': '', 'event_name': '전문성 신장을 위한 오르간 레슨비(1월~12월)', 'church_subsidy': 6000, 'self_funded': 0, 'total': 6000}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 반주단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
