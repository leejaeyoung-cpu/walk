import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 민족화해분과 생성 또는 가져오기
dept_id = create_department("민족화해분과")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '민족화해분과']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '분과장', 'name': '박은주', 'baptismal_name': '비비안나', 'contact': '010-5186-7005', 'region': '더타워'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': None, 'day': None, 'weekday': '월', 'event_name': '분기별 교구 민화위 분과모임(3,6,9,12월)', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 6, 'day': 7, 'weekday': '일', 'event_name': '평화특강', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 6, 'day': None, 'weekday': '', 'event_name': '민족의 화해와 일치를 위한 9일기도', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 12, 'day': 21, 'weekday': '월', 'event_name': '새터민지원센터 성탄선물 나눔', 'church_subsidy': 300, 'self_funded': 0, 'total': 300}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 민족화해분과")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
