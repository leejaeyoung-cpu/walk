import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 성가대 생성 또는 가져오기
dept_id = create_department("성가대")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '성가대']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장 및 단원', 'name': '정규상', 'baptismal_name': '야고보', 'contact': '010-8899-7404', 'region': '논현동'},
    {'position': '부단장 및 단원', 'name': '정윤영', 'baptismal_name': '아델라', 'contact': '010-3731-4026', 'region': '논현동'},
    {'position': '지휘자', 'name': '김유노', 'baptismal_name': '이냐시오', 'contact': '010-6310-9843', 'region': '시흥시'},
    {'position': '반주자', 'name': '배희정', 'baptismal_name': '타르실라', 'contact': '010-3352-1731', 'region': '논현동'},
    {'position': '총무', 'name': '전혜영', 'baptismal_name': '아녜스', 'contact': '010-3180-8710', 'region': '논현동'},
    {'position': '악보장', 'name': '최광섭', 'baptismal_name': '알베르또', 'contact': '010-4031-6790', 'region': '논현동'},
    {'position': '감사 및 단원', 'name': '유정복', 'baptismal_name': '사도요한', 'contact': '010-8181-8679', 'region': '논현동'},
    {'position': '고문 및 단원', 'name': '장슬기', 'baptismal_name': '세실리아', 'contact': '010-8721-3171', 'region': '논현동'},
    {'position': '단원', 'name': '송주형', 'baptismal_name': '요왕', 'contact': '010-6400-4427', 'region': '학익동'},
    {'position': '단원', 'name': '장연진', 'baptismal_name': '크리스티나', 'contact': '010-5282-7895', 'region': '논현동'},

    {'position': '단원', 'name': '김윤숙', 'baptismal_name': '소화데레사', 'contact': '010-9048-2757', 'region': '송도'},
    {'position': '단원', 'name': '권영은', 'baptismal_name': '로사', 'contact': '010-7303-0454', 'region': '논현동'},
    {'position': '단원', 'name': '배은숙', 'baptismal_name': '크리스티나', 'contact': '010-3577-0153', 'region': ''},
    {'position': '단원', 'name': '구희진', 'baptismal_name': '카타리나', 'contact': '010-4325-0429', 'region': '논현동'},
    {'position': '단원', 'name': '송민희', 'baptismal_name': '루치아', 'contact': '010-9248-2580', 'region': '논현동'},
    {'position': '단원', 'name': '이향선', 'baptismal_name': '로즈마리', 'contact': '010-9405-9516', 'region': '논현동'},
    {'position': '단원', 'name': '황효선', 'baptismal_name': '소피아', 'contact': '', 'region': '논현동'},

    {'position': '단원', 'name': '유정희', 'baptismal_name': '레아', 'contact': '010-8305-6035', 'region': '논현동'},
    {'position': '단원', 'name': '김명숙', 'baptismal_name': '미카엘라', 'contact': '', 'region': '논현동'},
    {'position': '단원', 'name': '전혜영', 'baptismal_name': '아녜스', 'contact': '010-3180-8710', 'region': '논현동'},
    {'position': '단원', 'name': '김은주', 'baptismal_name': '아녜스', 'contact': '010-5285-2339', 'region': '논현동'},
    {'position': '단원', 'name': '최광섭', 'baptismal_name': '알베르또', 'contact': '010-4031-6790', 'region': '논현동'},

    {'position': '단원', 'name': '한상만', 'baptismal_name': '아만도', 'contact': '010-8823-2339', 'region': '논현동'},


]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '신년미사(천주의 성모님 대축일) 성가 봉헌', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '성주간 성삼일 및 부활대축일 봉헌곡 준비', 'church_subsidy': 500, 'self_funded': 500, 'total': 1000},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '재의수요일 성가봉헌 및 성주간,부활성가준비', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 4, 'day': None, 'weekday': '', 'event_name': '성주간,부활대축일 성가봉헌 및 성모의 밤 행사 준비', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '성모의 밤 행사 성가 봉헌', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 6, 'day': None, 'weekday': '', 'event_name': '성가대 성지 피정', 'church_subsidy': 700, 'self_funded': 500, 'total': 1200},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '성당음악회 출연', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '성탄대축일 봉헌곡 준비', 'church_subsidy': 500, 'self_funded': 500, 'total': 1000},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '성탄대축일 미사 봉헌', 'church_subsidy': 0, 'self_funded': 0, 'total': 0}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 성가대")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
