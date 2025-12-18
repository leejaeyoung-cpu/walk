import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 어린이복사단자모회 생성 또는 가져오기
dept_id = create_department("어린이복사단자모회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '어린이복사단자모회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '회장', 'name': '유주희', 'baptismal_name': '바실리사', 'contact': '010-9258-8109', 'region': '에코'},
    {'position': '총무', 'name': '이은경', 'baptismal_name': '마리아', 'contact': '010-3554-6419', 'region': ''},
    {'position': '단원', 'name': '황은영', 'baptismal_name': '루시아', 'contact': '010-4209-0171', 'region': '기타'},
    {'position': '단원', 'name': '김영은', 'baptismal_name': '안젤라', 'contact': '010-3313-1659', 'region': '에코'},
    {'position': '단원', 'name': '신원지', 'baptismal_name': '마리아', 'contact': '010-4117-4935', 'region': '풍림'},
    {'position': '단원', 'name': '유선희', 'baptismal_name': '리디아', 'contact': '010-8960-7826', 'region': '에코'},
    {'position': '단원', 'name': '조현주', 'baptismal_name': '엘리사벳', 'contact': '010-2437-5321', 'region': '푸르내'},
    {'position': '단원', 'name': '전나리아', 'baptismal_name': '마리아', 'contact': '010-9356-4201', 'region': '에코'},
    {'position': '단원', 'name': '신현정', 'baptismal_name': '베로니카', 'contact': '010-6734-6926', 'region': '에코'},
    {'position': '단원', 'name': '이경순', 'baptismal_name': '소화데레사', 'contact': '010-9792-9194', 'region': '기타'},
    {'position': '단원', 'name': '최애경', 'baptismal_name': '로사', 'contact': '010-3554-6419', 'region': '에코'},
    {'position': '단원', 'name': '손묘하', 'baptismal_name': '레지나', 'contact': '010-4815-5422', 'region': '기타'},
    {'position': '단원', 'name': '김수용', 'baptismal_name': '비오', 'contact': '010-8077-2815', 'region': '기타'},
    {'position': '단원', 'name': '김병수', 'baptismal_name': '요셉', 'contact': '010-8917-4470', 'region': '푸르내'},
    {'position': '단원', 'name': '문경희', 'baptismal_name': '아네스', 'contact': '010-4728-9958', 'region': '기타'},
    {'position': '단원', 'name': '정다운', 'baptismal_name': '비비안나', 'contact': '010-7333-3223', 'region': '에코'},
    {'position': '단원', 'name': '이미나', 'baptismal_name': '글라라', 'contact': '010-2956-2505', 'region': '에코'},
    {'position': '단원', 'name': '유니나', 'baptismal_name': '율리아나', 'contact': '010-8910-1999', 'region': '푸르내'},
    {'position': '단원', 'name': '권영은', 'baptismal_name': '로사', 'contact': '010-7303-0454', 'region': '에코'},
    {'position': '단원', 'name': '정주희', 'baptismal_name': '마틸다', 'contact': '010-2325-4735', 'region': '에코'},
    {'position': '단원', 'name': '정은아', 'baptismal_name': '안젤라', 'contact': '010-9893-9865', 'region': '에코'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

print("\n=== 저장 완료 ===")
print(f"단체: 어린이복사단자모회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: 0건 (예산 정보 없음)")
