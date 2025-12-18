import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 어린이복사단 생성 또는 가져오기
dept_id = create_department("어린이복사단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '어린이복사단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '김민호', 'baptismal_name': '그레그리오', 'contact': '010-3194-4935', 'region': '풍림'},
    {'position': '부회장', 'name': '이도일', 'baptismal_name': '라파엘', 'contact': '010-4815-5422', 'region': '기타'},
    {'position': '단원', 'name': '김민수', 'baptismal_name': '요셉', 'contact': '', 'region': '기타'},
    {'position': '단원', 'name': '권한성', 'baptismal_name': '안젤로', 'contact': '010-2011-4735', 'region': '에코'},
    {'position': '단원', 'name': '신명철', 'baptismal_name': '마르티노', 'contact': '010-8470-4202', 'region': '에코'},
    {'position': '단원', 'name': '최진욱', 'baptismal_name': '바오로', 'contact': '010-5826-5321', 'region': '푸르내'},
    {'position': '단원', 'name': '권한나', 'baptismal_name': '안젤라', 'contact': '010-9411-4735', 'region': '에코'},
    {'position': '단원', 'name': '김준수', 'baptismal_name': '가브리엘', 'contact': '010-7446-9191', 'region': '기타'},
    {'position': '단원', 'name': '최시영', 'baptismal_name': '가브리엘', 'contact': '010-4169-5907', 'region': '에코'},
    {'position': '단원', 'name': '김유건', 'baptismal_name': '안드레아', 'contact': '010-8077-2815', 'region': '기타'},
    {'position': '단원', 'name': '서주완', 'baptismal_name': '레오', 'contact': '', 'region': '에코'},
    {'position': '단원', 'name': '최가현', 'baptismal_name': '미카엘라', 'contact': '010-2720-5231', 'region': '푸르내'},
    {'position': '단원', 'name': '이재원', 'baptismal_name': '요한크리소스토모', 'contact': '010-7535-8109', 'region': '에코'},
    {'position': '단원', 'name': '이지후', 'baptismal_name': '미카엘', 'contact': '010-7445-1659', 'region': '에코'},
    {'position': '단원', 'name': '이병록', 'baptismal_name': '요한보스코', 'contact': '010-4728-9958', 'region': '기타'},
    {'position': '단원', 'name': '김민교', 'baptismal_name': '데레사', 'contact': '010-8698-0171', 'region': '기타'},
    {'position': '단원', 'name': '송윤지', 'baptismal_name': '율리아', 'contact': '010-9157-1333', 'region': '푸르내'},
    {'position': '단원', 'name': '이예지', 'baptismal_name': '엘리사벳', 'contact': '010-2463-8109', 'region': '에코'},
    {'position': '단원', 'name': '박민아', 'baptismal_name': '미카엘라', 'contact': '', 'region': '에코'},
    {'position': '단원', 'name': '이서희', 'baptismal_name': '소화데레사', 'contact': '', 'region': '에코'},
    {'position': '단원', 'name': '김정민', 'baptismal_name': '로베르토', 'contact': '010-8971-4470', 'region': '푸르내'},
    {'position': '단원', 'name': '김서현', 'baptismal_name': '세실리아', 'contact': '010-5622-9865', 'region': '에코'},
    {'position': '단원', 'name': '송윤제', 'baptismal_name': '요셉', 'contact': '010-5073-2666', 'region': '푸르내'},
    {'position': '단원', 'name': '이자인', 'baptismal_name': '레지나', 'contact': '010-5536-1320', 'region': '에코'},
    {'position': '단원', 'name': '박영민', 'baptismal_name': '대건안드레아', 'contact': '010-7651-8422', 'region': '에코'},
    {'position': '단원', 'name': '최바로', 'baptismal_name': '레오', 'contact': '010-8316-6233', 'region': '에코'}
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
print(f"단체: 어린이복사단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
