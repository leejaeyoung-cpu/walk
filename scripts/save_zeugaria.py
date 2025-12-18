import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 즈가리아복사단 생성 또는 가져오기
dept_id = create_department("즈가리아복사단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '즈가리아복사단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장', 'name': '유병택', 'baptismal_name': '에우카리오', 'contact': '010-4720-9934', 'region': '시흥'},
    {'position': '회계', 'name': '박상용', 'baptismal_name': '대건안드레아', 'contact': '010-2470-2148', 'region': '에코12'},
    {'position': '단원', 'name': '나견주', 'baptismal_name': '요한보스코', 'contact': '010-8864-1670', 'region': '에코11'},
    {'position': '단원', 'name': '이계양', 'baptismal_name': '요셉', 'contact': '010-5412-6142', 'region': '에코12'},
    {'position': '단원', 'name': '차병현', 'baptismal_name': '빈첸시오', 'contact': '010-3334-8577', 'region': '더타워'},
    {'position': '단원', 'name': '황치성', 'baptismal_name': '베드로', 'contact': '010-6788-3774', 'region': '에코5'},
    {'position': '단원', 'name': '김형석', 'baptismal_name': '파스칼', 'contact': '010-4182-3780', 'region': '풍림'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 2, 'day': None, 'weekday': '일', 'event_name': '신년회', 'church_subsidy': 0, 'self_funded': 200, 'total': 200},
    {'month': 6, 'day': None, 'weekday': '일', 'event_name': '성지 순례', 'church_subsidy': 0, 'self_funded': 200, 'total': 200},
    {'month': 7, 'day': None, 'weekday': '토', 'event_name': '여름 친목 모임', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 10, 'day': None, 'weekday': '토', 'event_name': '성지 순례', 'church_subsidy': 0, 'self_funded': 200, 'total': 200},
    {'month': 12, 'day': None, 'weekday': '금', 'event_name': '송년회', 'church_subsidy': 0, 'self_funded': 500, 'total': 500}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 즈가리아복사단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
