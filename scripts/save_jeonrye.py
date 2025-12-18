import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 전례분과 생성 또는 가져오기
dept_id = create_department("전례분과")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '전례분과']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '분과장', 'name': '박상용', 'baptismal_name': '대건안드레아', 'contact': '010-2470-2148', 'region': '에코12'},
    {'position': '총무', 'name': '김슬기', 'baptismal_name': '파비올라', 'contact': '010-9947-5386', 'region': '더타워'},
    {'position': '회원', 'name': '김원경', 'baptismal_name': '카타리나', 'contact': '010-5285-0351', 'region': '에코12'},
    {'position': '회원', 'name': '박은주', 'baptismal_name': '비비안나', 'contact': '010-5186-7005', 'region': '더타워'},
    {'position': '회원', 'name': '박현아', 'baptismal_name': '이사벨라', 'contact': '010-5156-5416', 'region': '-'},
    {'position': '회원', 'name': '정규상', 'baptismal_name': '야고보', 'contact': '010-8899-7404', 'region': '논현동'},
    {'position': '회원', 'name': '정주희', 'baptismal_name': '마틸다', 'contact': '010-2325-4735', 'region': '에코12'},
    {'position': '회원', 'name': '김경순', 'baptismal_name': '데레사', 'contact': '010-6327-9956', 'region': '에코6'},
    {'position': '회원', 'name': '심상문', 'baptismal_name': '야고보', 'contact': '', 'region': '-'},
    {'position': '회원', 'name': '유병택', 'baptismal_name': '에우카리오', 'contact': '010-4720-9934', 'region': '시흥'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': None, 'day': None, 'weekday': '토', 'event_name': '전례분과 단체장 정기회의', 'church_subsidy': 0, 'self_funded': 1200, 'total': 1200},
    {'month': 1, 'day': None, 'weekday': '토', 'event_name': '전례분과 상반기 친목회', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 7, 'day': None, 'weekday': '토', 'event_name': '전례분과 하반기 친목회', 'church_subsidy': 0, 'self_funded': 500, 'total': 500}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 전례분과")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
