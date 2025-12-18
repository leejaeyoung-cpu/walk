import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 중고등교리교사회 생성 또는 가져오기
dept_id = create_department("중고등교리교사회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '중고등교리교사회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '교감', 'name': '조현주', 'baptismal_name': '엘리사벳', 'contact': '010-2437-5321', 'region': '13단지'},
    {'position': '교사', 'name': '한희경', 'baptismal_name': '아나니아', 'contact': '010-4702-1803', 'region': '11단지'},
    {'position': '교사', 'name': '김슬기', 'baptismal_name': '파비올라', 'contact': '010-9947-5386', 'region': '더타워'},
    {'position': '교사', 'name': '김수용', 'baptismal_name': '비오', 'contact': '010-8077-2815', 'region': '삼산동(기타)'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': None, 'day': None, 'weekday': '', 'event_name': '음악미사(주경야락) 2025.12-2026.11', 'church_subsidy': 1200, 'self_funded': 0, 'total': 1200},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '음악미사(김성식, 신상훈) 2025.12-2026.11', 'church_subsidy': 1200, 'self_funded': 0, 'total': 1200},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '매월 주일학교 교리준비비 2025.12-2026.11', 'church_subsidy': 240, 'self_funded': 0, 'total': 240},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '간식비 2025.12-2026.11', 'church_subsidy': 4200, 'self_funded': 0, 'total': 4200},
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '전례부 단합 회식', 'church_subsidy': 150, 'self_funded': 0, 'total': 150},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '장기근속 교리교사 지원비(해외성지순례)', 'church_subsidy': 1000, 'self_funded': 1000, 'total': 2000},
    {'month': 2, 'day': 28, 'weekday': '토', 'event_name': '종업식 및 졸업식', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 3, 'day': 7, 'weekday': '토', 'event_name': '입학식 및 삼겹살데이(입학축하파티)', 'church_subsidy': 300, 'self_funded': 0, 'total': 300},
    {'month': 4, 'day': 4, 'weekday': '토', 'event_name': '부활대축일', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 4, 'day': 26, 'weekday': '일', 'event_name': '성소주일행사', 'church_subsidy': 0, 'self_funded': 150, 'total': 150},
    {'month': 5, 'day': 23, 'weekday': '토', 'event_name': '청소년주일 행사(남동지구연합)', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': 6, 'day': 20, 'weekday': '토', 'event_name': '문화 day', 'church_subsidy': 600, 'self_funded': 0, 'total': 600},
    {'month': 8, 'day': 23, 'weekday': '일', 'event_name': '여름행사(물놀이)', 'church_subsidy': 2400, 'self_funded': 600, 'total': 3000},
    {'month': 9, 'day': 12, 'weekday': '토', 'event_name': '성지순례(이승훈베드로기념관)', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 11, 'day': 28, 'weekday': '토', 'event_name': '중고등부 피정(안드레아 피정의 집)', 'church_subsidy': 1500, 'self_funded': 600, 'total': 2100},
    {'month': 11, 'day': 29, 'weekday': '일', 'event_name': '난방비', 'church_subsidy': 300, 'self_funded': 0, 'total': 300},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '위탁비용(피정위탁)', 'church_subsidy': 300, 'self_funded': 0, 'total': 300}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 중고등교리교사회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
print(f"총 예산: 14,240천원")
