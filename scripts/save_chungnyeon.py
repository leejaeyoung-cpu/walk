import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 청년회 생성 또는 가져오기
dept_id = create_department("청년회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '청년회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '권용훈', 'baptismal_name': '미카엘', 'contact': '010-9975-7964', 'region': '호구포'},
    {'position': '부회장', 'name': '송혜은', 'baptismal_name': '비비안나', 'contact': '010-7193-4389', 'region': '소래'},
    {'position': '총무', 'name': '정유찬', 'baptismal_name': '요셉', 'contact': '010-8294-1130', 'region': '소래'},
    {'position': '단원', 'name': '강호송', 'baptismal_name': '대건안드레아', 'contact': '010-8223-9774', 'region': '소래'},
    {'position': '단원', 'name': '권준완', 'baptismal_name': '안드레아', 'contact': '010-5064-4349', 'region': '소래'},
    {'position': '단원', 'name': '김세원', 'baptismal_name': '헬레나', 'contact': '010-9007-7906', 'region': '영종도'},
    {'position': '단원', 'name': '서장원', 'baptismal_name': '마르코', 'contact': '010-8984-9821', 'region': '소래'},
    {'position': '단원', 'name': '양순주', 'baptismal_name': '바오로', 'contact': '010-7563-8897', 'region': '호구포'},
    {'position': '단원', 'name': '이승민', 'baptismal_name': '필립보', 'contact': '010-4560-7932', 'region': '소래'},
    {'position': '단원', 'name': '이지민', 'baptismal_name': '세실리아', 'contact': '010-2558-2956', 'region': '소래'},
    {'position': '단원', 'name': '전혜영', 'baptismal_name': '아녜스', 'contact': '010-3180-8710', 'region': '소래'},
    {'position': '단원', 'name': '조가영', 'baptismal_name': '안나', 'contact': '010-4010-7186', 'region': '소래'},
    {'position': '단원', 'name': '한대연', 'baptismal_name': '요한', 'contact': '010-4007-2911', 'region': '만수동'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': 1, 'day': 4, 'weekday': '일', 'event_name': '1월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 1, 'day': None, 'weekday': '일', 'event_name': '신부님과 식사', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': 1, 'day': 25, 'weekday': '토', 'event_name': '친목활동(1) - 미정', 'church_subsidy': 500, 'self_funded': 500, 'total': 1000},
    {'month': 3, 'day': 1, 'weekday': '일', 'event_name': '청년회 홍보 포스터 부착', 'church_subsidy': 20, 'self_funded': 0, 'total': 20},
    {'month': 3, 'day': 1, 'weekday': '일', 'event_name': '3월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 3, 'day': 15, 'weekday': '일', 'event_name': '신부님 영명 축일 선물', 'church_subsidy': 50, 'self_funded': 0, 'total': 50},
    {'month': 4, 'day': 5, 'weekday': '일', 'event_name': '4월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 4, 'day': None, 'weekday': '일', 'event_name': '수익사업 (1) - 미정', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 5, 'day': 3, 'weekday': '일', 'event_name': '5월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 5, 'day': None, 'weekday': '토', 'event_name': '친목활동 (2) - 미정', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 6, 'day': 7, 'weekday': '일', 'event_name': '6월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 7, 'day': 5, 'weekday': '일', 'event_name': '7월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 7, 'day': None, 'weekday': '토,일', 'event_name': '친목활동(3) - 하계 MT', 'church_subsidy': 500, 'self_funded': 500, 'total': 1000},
    {'month': 8, 'day': 2, 'weekday': '일', 'event_name': '8월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 9, 'day': 6, 'weekday': '일', 'event_name': '9월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '수익사업(2) - 일일호프', 'church_subsidy': 1500, 'self_funded': 0, 'total': 1500},
    {'month': 11, 'day': 1, 'weekday': '일', 'event_name': '11월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 11, 'day': 9, 'weekday': '일', 'event_name': '수험생 선물', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 12, 'day': 6, 'weekday': '일', 'event_name': '12월 축일자 생미사', 'church_subsidy': 30, 'self_funded': 0, 'total': 30},
    {'month': 12, 'day': 28, 'weekday': '일', 'event_name': '친목활동(4) - 송년회', 'church_subsidy': 300, 'self_funded': 0, 'total': 300}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 청년회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
