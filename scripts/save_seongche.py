import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 성체분배회 생성 또는 가져오기
dept_id = create_department("성체분배회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '성체분배회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '이병찬', 'baptismal_name': '베드로', 'contact': '010-2918-8700', 'region': '시흥'},
    {'position': '총무', 'name': '조정현', 'baptismal_name': '토마스', 'contact': '010-5292-7186', 'region': '에코11'},
    {'position': '회원', 'name': '여동춘', 'baptismal_name': '프란시스코 사베리오', 'contact': '010-3661-9956', 'region': '에코6'},
    {'position': '회원', 'name': '류정현', 'baptismal_name': '다니엘', 'contact': '010-5310-9828', 'region': '에코11'},
    {'position': '회원', 'name': '이규인', 'baptismal_name': '바울리노', 'contact': '010-5772-6731', 'region': '주공13'},
    {'position': '회원', 'name': '우제남', 'baptismal_name': '야고보', 'contact': '010-3319-8218', 'region': '에코12'},
    {'position': '회원', 'name': '이용우', 'baptismal_name': '바오로', 'contact': '010-8722-9378', 'region': '에코12'},
    {'position': '회원', 'name': '김창진', 'baptismal_name': '가브리엘', 'contact': '010-9019-4147', 'region': '풍림'},
    {'position': '회원', 'name': '유병택', 'baptismal_name': '에우카리오', 'contact': '010-4720-9934', 'region': '시흥'},
    {'position': '회원', 'name': '정영교', 'baptismal_name': '제오르지오', 'contact': '010-3859-6184', 'region': '에코6'},
    {'position': '회원', 'name': '송주형', 'baptismal_name': '요왕', 'contact': '010-6400-4427', 'region': '풍림'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 3, 'day': 10, 'weekday': '수', 'event_name': '성체분배복 세탁', 'church_subsidy': 0, 'self_funded': 120, 'total': 120},
    {'month': 5, 'day': 23, 'weekday': '토', 'event_name': '신입회원 환영회', 'church_subsidy': 0, 'self_funded': 600, 'total': 600},
    {'month': 5, 'day': 29, 'weekday': '금', 'event_name': '성모의밤 화분봉헌', 'church_subsidy': 0, 'self_funded': 100, 'total': 100},
    {'month': 7, 'day': 25, 'weekday': '토', 'event_name': '성체분배회 친목 복달임', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 9, 'day': 12, 'weekday': '토', 'event_name': '성체분배회 성지순례', 'church_subsidy': 0, 'self_funded': 500, 'total': 500},
    {'month': 12, 'day': 18, 'weekday': '금', 'event_name': '성체분배회 송년회', 'church_subsidy': 0, 'self_funded': 600, 'total': 600}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 성체분배회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
