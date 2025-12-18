import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 초등교리교사회 생성 또는 가져오기
dept_id = create_department("초등교리교사회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '초등교리교사회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '교감', 'name': '박은주', 'baptismal_name': '비비안나', 'contact': '010-5186-7005', 'region': '더타워'},
    {'position': '총무', 'name': '유선희', 'baptismal_name': '리디아', 'contact': '010-8960-7826', 'region': '에코 9단지(기타)'},
    {'position': '교사', 'name': '강민아', 'baptismal_name': '글라라', 'contact': '', 'region': '풍림'},
    {'position': '교사', 'name': '김영은', 'baptismal_name': '안젤라', 'contact': '', 'region': '에코6단지'},
    {'position': '교사', 'name': '전지혁', 'baptismal_name': '빅토리노', 'contact': '', 'region': '소래'},
    {'position': '교사', 'name': '김연진', 'baptismal_name': '율리안나', 'contact': '', 'region': '송림동(기타)'},
    {'position': '교사', 'name': '박은자', 'baptismal_name': '바실라', 'contact': '', 'region': '도화동(기타)'},
    {'position': '교사', 'name': '전나리아', 'baptismal_name': '마리아', 'contact': '', 'region': '에코6단지'},
    {'position': '교사', 'name': '최애경', 'baptismal_name': '로사', 'contact': '', 'region': '에코12단지'},
    {'position': '교사', 'name': '박현숙', 'baptismal_name': '젤뚜르다', 'contact': '', 'region': '에코12단지'},
    {'position': '교사', 'name': '안지연', 'baptismal_name': '율리안나', 'contact': '', 'region': '풍림'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': None, 'day': None, 'weekday': '', 'event_name': '음악미사(주경야락) 2025.12-2026.11', 'church_subsidy': 1200, 'self_funded': 0, 'total': 1200},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '음악미사(김성식, 신상훈) 2025.12-2026.11', 'church_subsidy': 1200, 'self_funded': 0, 'total': 1200},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '매월 주일학교 운영비 2025.12-2026.11', 'church_subsidy': 3600, 'self_funded': 0, 'total': 3600},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '교리교사 안전교육(청소년사목국) 2024.12-2025.11', 'church_subsidy': 140, 'self_funded': 0, 'total': 140},
    {'month': 12, 'day': 25, 'weekday': '수', 'event_name': '성탄선물 나눔 2025/12', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '교리교사 수첩 구입', 'church_subsidy': 105, 'self_funded': 0, 'total': 105},
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '전례부 단합 회식', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 1, 'day': 3, 'weekday': '토', 'event_name': '애니어그램부모교육', 'church_subsidy': 450, 'self_funded': 0, 'total': 450},
    {'month': 1, 'day': 15, 'weekday': '목', 'event_name': '6학년 졸업여행(롯데월드)', 'church_subsidy': 700, 'self_funded': 0, 'total': 700},
    {'month': 1, 'day': 16, 'weekday': '금', 'event_name': '신입교리교사연수(2박3일 - 청소년사목국)', 'church_subsidy': 540, 'self_funded': 0, 'total': 540},
    {'month': 1, 'day': 26, 'weekday': '월', 'event_name': '교리교사 아카데미2단계 1학기(2/24까지)', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '캠프 답사비', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 2, 'day': 28, 'weekday': '토', 'event_name': '종업식 및 졸업식', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '초등부 주일학교 교리교재 구입', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 4, 'day': 19, 'weekday': '일', 'event_name': '전례연수(청소년사목국)', 'church_subsidy': 105, 'self_funded': 0, 'total': 105},
    {'month': 4, 'day': 26, 'weekday': '일', 'event_name': '성소주일행사', 'church_subsidy': 0, 'self_funded': 150, 'total': 150},
    {'month': 5, 'day': 2, 'weekday': '토', 'event_name': '은총시장', 'church_subsidy': 2500, 'self_funded': 0, 'total': 2500},
    {'month': 5, 'day': 16, 'weekday': '토', 'event_name': '스승의 날 교사 선물구입비', 'church_subsidy': 300, 'self_funded': 0, 'total': 300},
    {'month': 6, 'day': None, 'weekday': '', 'event_name': '레크레이션 연수(청소년 사목국)', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': 6, 'day': 13, 'weekday': '토', 'event_name': '근속교리교사피정(1박2일 – 청소년사목국)', 'church_subsidy': 390, 'self_funded': 0, 'total': 390},
    {'month': 7, 'day': None, 'weekday': '', 'event_name': '초등부여름신앙캠프(1박2일)', 'church_subsidy': 5000, 'self_funded': 900, 'total': 5900},
    {'month': 8, 'day': None, 'weekday': '', 'event_name': '저학년물놀이', 'church_subsidy': 600, 'self_funded': 150, 'total': 750},
    {'month': 8, 'day': 24, 'weekday': '월', 'event_name': '교리교사 아카데미 2단계 2학기(9/15까지)', 'church_subsidy': 200, 'self_funded': 0, 'total': 200},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '초등부성지순례(이승훈베드로성지)', 'church_subsidy': 450, 'self_funded': 0, 'total': 450},
    {'month': 10, 'day': 18, 'weekday': '일', 'event_name': '교리교사의 날 행사(청소년사목국)', 'church_subsidy': 900, 'self_funded': 0, 'total': 900},
    {'month': 10, 'day': 31, 'weekday': '토', 'event_name': '첫영성체 가족피정', 'church_subsidy': 800, 'self_funded': 0, 'total': 800},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '남동지구 연합미사 행사', 'church_subsidy': 400, 'self_funded': 0, 'total': 400},
    {'month': 11, 'day': 8, 'weekday': '일', 'event_name': '실무자대표연수(청소년사목국)', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 11, 'day': 21, 'weekday': '토', 'event_name': '첫영성체 행사(상품비 포함)', 'church_subsidy': 400, 'self_funded': 210, 'total': 610},
    {'month': 11, 'day': 28, 'weekday': '토', 'event_name': '교리교사피정(1박2일-청소년사목국)', 'church_subsidy': 260, 'self_funded': 0, 'total': 260},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '예비비', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 초등교리교사회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
