import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 초등부자모회 생성 또는 가져오기
dept_id = create_department("초등부자모회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '초등부자모회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '정은아', 'baptismal_name': '안젤라', 'contact': '010-9893-9865', 'region': ''},
    {'position': '총무', 'name': '유니나', 'baptismal_name': '율리안나', 'contact': '010-8910-1999', 'region': ''},
    {'position': '부회장', 'name': '조정현', 'baptismal_name': '마더데레사', 'contact': '010-9114-7316', 'region': ''},
    {'position': '회원', 'name': '정다운', 'baptismal_name': '비비안나', 'contact': '010-7333-3223', 'region': ''},
    {'position': '회원', 'name': '차은옥', 'baptismal_name': '보나', 'contact': '010-5205-8945', 'region': ''},
    {'position': '회원', 'name': '김병수', 'baptismal_name': '요셉', 'contact': '010-8917-4470', 'region': ''},
    {'position': '회원', 'name': '정혜주', 'baptismal_name': '첼리인나', 'contact': '010-2765-8287', 'region': ''},
    {'position': '회원', 'name': '김애희', 'baptismal_name': '사비나', 'contact': '010-9896-7161', 'region': ''},
    {'position': '회원', 'name': '이은경', 'baptismal_name': '마리아', 'contact': '010-3554-6419', 'region': ''},
    {'position': '회원', 'name': '이은희', 'baptismal_name': '사비나', 'contact': '010-6367-1792', 'region': ''},
    {'position': '회원', 'name': '이미경', 'baptismal_name': '안젤라', 'contact': '010-6328-8718', 'region': ''},
    {'position': '회원', 'name': '오정화', 'baptismal_name': '첼리나', 'contact': '010-6859-4952', 'region': ''},
    {'position': '회원', 'name': '유주희', 'baptismal_name': '바실리사', 'contact': '010-9258-8109', 'region': ''},
    {'position': '회원', 'name': '이미나', 'baptismal_name': '글라라', 'contact': '010-2956-2505', 'region': ''},
    {'position': '회원', 'name': '배승희', 'baptismal_name': '카타리나', 'contact': '010-3878-8774', 'region': ''},
    {'position': '회원', 'name': '손원경', 'baptismal_name': '카타리나', 'contact': '010-9658-1207', 'region': ''},
    {'position': '회원', 'name': '신현정', 'baptismal_name': '베로니카', 'contact': '010-6734-6926', 'region': ''},
    {'position': '회원', 'name': '채상희', 'baptismal_name': '마리아', 'contact': '010-5475-4810', 'region': ''},
    {'position': '회원', 'name': '고은영', 'baptismal_name': '스텔라', 'contact': '010-3163-8278', 'region': ''},
    {'position': '회원', 'name': '황재준', 'baptismal_name': '율리아노', 'contact': '010-8863-1128', 'region': ''},
    {'position': '회원', 'name': '박가윤', 'baptismal_name': '레지나', 'contact': '010-8882-2765', 'region': ''},
    {'position': '회원', 'name': '권미경', 'baptismal_name': '프란체스카', 'contact': '010-6428-4070', 'region': ''},
    {'position': '회원', 'name': '주하나', 'baptismal_name': '루시아', 'contact': '010-9017-2209', 'region': ''},
    {'position': '회원', 'name': '조하나', 'baptismal_name': '헬레나', 'contact': '010-9336-4523', 'region': ''},
    {'position': '회원', 'name': '김혜미', 'baptismal_name': '엘리사벳', 'contact': '010-2173-9620', 'region': ''},
    {'position': '회원', 'name': '서정희', 'baptismal_name': '베로니카', 'contact': '010-9550-2017', 'region': ''},
    {'position': '회원', 'name': '이지혜', 'baptismal_name': '소피아', 'contact': '010-8999-5057', 'region': ''},
    {'position': '회원', 'name': '조세은', 'baptismal_name': '플라비아', 'contact': '010-6339-3891', 'region': ''},
    {'position': '회원', 'name': '이윤경', 'baptismal_name': '젬마', 'contact': '010-8952-4144', 'region': ''},
    {'position': '회원', 'name': '윤수민', 'baptismal_name': '안젤라', 'contact': '010-9379-2613', 'region': ''},
    {'position': '회원', 'name': '박미혜', 'baptismal_name': '', 'contact': '010-8932-5426', 'region': ''},
    {'position': '회원', 'name': '손지은', 'baptismal_name': '비비안나', 'contact': '010-4592-2920', 'region': ''},
    {'position': '회원', 'name': '권미경', 'baptismal_name': '프란체스카', 'contact': '010-6428-4070', 'region': ''},
    {'position': '회원', 'name': '황은영', 'baptismal_name': '루시아', 'contact': '010-4309-0171', 'region': ''},
    {'position': '회원', 'name': '김효재', 'baptismal_name': '사라', 'contact': '010-5777-9386', 'region': ''}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 600, 'self_funded': 0, 'total': 600},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 4, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 600, 'self_funded': 0, 'total': 600},
    {'month': 6, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 7, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 8, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 600, 'self_funded': 0, 'total': 600},
    {'month': 9, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 600, 'self_funded': 0, 'total': 600},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '간식비', 'church_subsidy': 500, 'self_funded': 0, 'total': 500},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '자모회식사비', 'church_subsidy': 375, 'self_funded': 0, 'total': 375}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 초등부자모회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
