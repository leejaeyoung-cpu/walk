import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 성인복사단 생성 또는 가져오기
dept_id = create_department("성인복사단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '성인복사단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장', 'name': '심상문', 'baptismal_name': '야고보', 'contact': '010-8343-7000', 'region': '에코5구역'},
    {'position': '부단장', 'name': '나성주', 'baptismal_name': '젤마노', 'contact': '010-3741-1150', 'region': '기타구역'},
    {'position': '총무', 'name': '서준혁', 'baptismal_name': '안드레아', 'contact': '010-4808-4349', 'region': '풍림구역'},
    {'position': '회계', 'name': '전형준', 'baptismal_name': '바오로', 'contact': '010-9331-6425', 'region': '기타구역'},
    {'position': '단원', 'name': '김학진', 'baptismal_name': '안토니오', 'contact': '010-3213-4041', 'region': '에코6구역'},
    {'position': '단원', 'name': '이정철', 'baptismal_name': '베드로', 'contact': '010-9913-7441', 'region': '에코5구역'},
    {'position': '단원', 'name': '김수용', 'baptismal_name': '비오', 'contact': '010-8077-2815', 'region': '기타구역'},
    {'position': '단원', 'name': '오승배', 'baptismal_name': '빈첸시오', 'contact': '010-8230-0501', 'region': '에코6구역'},
    {'position': '단원', 'name': '천세진', 'baptismal_name': '베드로', 'contact': '010-2488-2066', 'region': '유호,푸르지오 구역'},
    {'position': '단원', 'name': '이재영', 'baptismal_name': '바오로', 'contact': '010-6517-1320', 'region': '에코6구역'},
    {'position': '단원', 'name': '박보선', 'baptismal_name': '프란치스코', 'contact': '010-5234-8422', 'region': '에코11구역'},
    {'position': '단원', 'name': '이기웅', 'baptismal_name': '이냐시오', 'contact': '010-9142-6677', 'region': '에코12구역'},
    {'position': '단원', 'name': '최원', 'baptismal_name': '가브리엘', 'contact': '010-5234-8422', 'region': '기타구역'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 7, 'day': 11, 'weekday': '토', 'event_name': '성지순례', 'church_subsidy': 0, 'self_funded': 300, 'total': 300}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 성인복사단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
