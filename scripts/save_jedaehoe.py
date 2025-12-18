import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 제대회 생성 또는 가져오기
dept_id = create_department("제대회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '제대회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '김원경', 'baptismal_name': '카타리나', 'contact': '010-5285-0351', 'region': '11구역'},
    {'position': '총무', 'name': '이희연', 'baptismal_name': '스텔라', 'contact': '010-3441-7383', 'region': '6구역'},
    {'position': '단원', 'name': '박정순', 'baptismal_name': '요셉피나', 'contact': '010-3519-9378', 'region': '12구역'},
    {'position': '단원', 'name': '전주영', 'baptismal_name': '세실리아', 'contact': '010-4856-6936', 'region': '6구역'},
    {'position': '단원', 'name': '강헌숙', 'baptismal_name': '안젤라', 'contact': '010-2600-1233', 'region': '12구역'},
    {'position': '단원', 'name': '임성순', 'baptismal_name': '모니카', 'contact': '010-6283-7186', 'region': '11구역'},
    {'position': '단원', 'name': '김인숙', 'baptismal_name': '아네스', 'contact': '010-9907-2956', 'region': '11구역'},
    {'position': '단원', 'name': '이지영', 'baptismal_name': '이라이스', 'contact': '010-7763-6143', 'region': '14구역'},
    {'position': '단원', 'name': '오윤선', 'baptismal_name': '아가다', 'contact': '010-8964-4797', 'region': '6구역'},
    {'position': '단원', 'name': '장명숙', 'baptismal_name': '안나', 'contact': '010-3907-1048', 'region': '12구역'},
    {'position': '단원', 'name': '이애경', 'baptismal_name': '마리아', 'contact': '010-2339-9792', 'region': '소래구역'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '전례력,숯향,제대초 구입', 'church_subsidy': 469, 'self_funded': 0, 'total': 469},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '제병구입', 'church_subsidy': 555, 'self_funded': 0, 'total': 555},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '제병구입', 'church_subsidy': 405, 'self_funded': 0, 'total': 405},
    {'month': 7, 'day': None, 'weekday': '', 'event_name': '제병구입', 'church_subsidy': 505, 'self_funded': 0, 'total': 505},
    {'month': 8, 'day': None, 'weekday': '', 'event_name': '숯향,주수잔 구입', 'church_subsidy': 170, 'self_funded': 0, 'total': 170},
    {'month': 9, 'day': None, 'weekday': '', 'event_name': '제병구입', 'church_subsidy': 505, 'self_funded': 0, 'total': 505},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '미사주,제병 구입', 'church_subsidy': 504, 'self_funded': 0, 'total': 504},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '제대소모품 구입(1~12월)', 'church_subsidy': 250, 'self_funded': 0, 'total': 250},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '세탁비(1~12월)', 'church_subsidy': 157, 'self_funded': 0, 'total': 157},
    {'month': None, 'day': 4, 'weekday': '수', 'event_name': '제대회 월례회의(년중 4주 수요일) 10명*10', 'church_subsidy': 0, 'self_funded': 1200, 'total': 1200}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 제대회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
