import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 헌화회 생성 또는 가져오기
dept_id = create_department("헌화회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '헌화회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '김경순', 'baptismal_name': '데레사', 'contact': '010-6327-9956', 'region': '에코6'},
    {'position': '회원', 'name': '배승자', 'baptismal_name': '아가다', 'contact': '010-8833-2079', 'region': '주공14'},
    {'position': '회원', 'name': '김재숙', 'baptismal_name': '소피아', 'contact': '010-4702-2353', 'region': '에코12'},
    {'position': '회원', 'name': '강은미', 'baptismal_name': '안젤라', 'contact': '010-3301-8664', 'region': '유호'},
    {'position': '회원', 'name': '박정아', 'baptismal_name': '미카엘라', 'contact': '010-2912-7993', 'region': '에코5'},
    {'position': '회원', 'name': '이진희', 'baptismal_name': '소화데레사', 'contact': '010-6737-9029', 'region': '에코6'},
    {'position': '회원', 'name': '강현정', 'baptismal_name': '미카엘라', 'contact': '010-5473-3407', 'region': '에코6'},
    {'position': '회원', 'name': '윤미연', 'baptismal_name': '안젤라', 'contact': '010-9964-2066', 'region': '푸르지오'},
    {'position': '회원', 'name': '오정화', 'baptismal_name': '첼리나', 'contact': '010-6859-4952', 'region': '에코6'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': None, 'day': None, 'weekday': '', 'event_name': '제대 꽃 봉헌 (1월~12월)', 'church_subsidy': 0, 'self_funded': 3130, 'total': 3130},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '성모의 밤', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '대림시기', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '주님성탄대축일', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': None, 'day': None, 'weekday': '금', 'event_name': '헌화회 월례회의 (매월 4주)', 'church_subsidy': 0, 'self_funded': 900, 'total': 900},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '화훼단지 견학(고양)', 'church_subsidy': 270, 'self_funded': 0, 'total': 270}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 헌화회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
