import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 독서단 생성 또는 가져오기
dept_id = create_department("독서단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '독서단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장', 'name': '박현아', 'baptismal_name': '이사벨라', 'contact': '010-5156-5416', 'region': ''},
    {'position': '부단장', 'name': '김은주', 'baptismal_name': '아녜스', 'contact': '010-5285-2339', 'region': ''},
    {'position': '단원', 'name': '가연숙', 'baptismal_name': '스텔라', 'contact': '010-9381-4353', 'region': ''},
    {'position': '단원', 'name': '강기정', 'baptismal_name': '데레사', 'contact': '010-4527-2821', 'region': ''},
    {'position': '단원', 'name': '김순녀', 'baptismal_name': '루시아', 'contact': '010-2355-7722', 'region': ''},
    {'position': '단원', 'name': '김순민', 'baptismal_name': '글로리아', 'contact': '010-6226-1113', 'region': ''},
    {'position': '단원', 'name': '류수환', 'baptismal_name': '스테파노', 'contact': '010-8781-5252', 'region': ''},
    {'position': '단원', 'name': '박장석', 'baptismal_name': '토마스', 'contact': '010-3306-2931', 'region': ''},
    {'position': '단원', 'name': '서병각', 'baptismal_name': '바오로', 'contact': '010-2733-8045', 'region': ''},
    {'position': '단원', 'name': '신정자', 'baptismal_name': '골롬바', 'contact': '010-3799-7285', 'region': ''},
    {'position': '단원', 'name': '오금순', 'baptismal_name': '리디아', 'contact': '010-8363-0864', 'region': ''},
    {'position': '단원', 'name': '오필숙', 'baptismal_name': '아녜스', 'contact': '010-3200-2605', 'region': ''},
    {'position': '단원', 'name': '이승언', 'baptismal_name': '글라라', 'contact': '010-2393-7479', 'region': ''},
    {'position': '단원', 'name': '이은희', 'baptismal_name': '마리아', 'contact': '010-5299-9934', 'region': ''},
    {'position': '단원', 'name': '전인수', 'baptismal_name': '요셉', 'contact': '010-8872-4478', 'region': ''},
    {'position': '단원', 'name': '정희연', 'baptismal_name': '베로니카', 'contact': '010-2131-5040', 'region': ''},
    {'position': '단원', 'name': '조영순', 'baptismal_name': '모니카', 'contact': '010-8283-5620', 'region': ''},
    {'position': '단원', 'name': '한상순', 'baptismal_name': '시몬', 'contact': '010-9319-5265', 'region': ''},
    {'position': '단원', 'name': '호미선', 'baptismal_name': '율리아나', 'contact': '010-3409-4256', 'region': ''},
    {'position': '단원', 'name': '황치성', 'baptismal_name': '베드로', 'contact': '010-6788-3774', 'region': ''}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 1, 'day': 7, 'weekday': '수', 'event_name': '사제서품 참가', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '복사 봉사 후 아이들 간식', 'church_subsidy': 0, 'self_funded': 1200, 'total': 1200},
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '축일축하 문화상품권 지급', 'church_subsidy': 0, 'self_funded': 300, 'total': 300},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '단원 프로필 사진 촬영', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '신입 단원 환영회', 'church_subsidy': 0, 'self_funded': 300, 'total': 300},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '스포츠데이(연6회) 식사 및 입장권', 'church_subsidy': 1200, 'self_funded': 180, 'total': 400},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '전례교육간식 및 격려상품', 'church_subsidy': 300, 'self_funded': 200, 'total': 200},
    {'month': 4, 'day': None, 'weekday': '', 'event_name': '복사복 세탁비', 'church_subsidy': 0, 'self_funded': 200, 'total': 200},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '복사단원 및 자모회성탄모임', 'church_subsidy': 500, 'self_funded': 200, 'total': 600},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '겨울 신앙 캠프', 'church_subsidy': 500, 'self_funded': 500, 'total': 1000}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 독서단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
