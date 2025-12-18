import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 해설단 생성 또는 가져오기
dept_id = create_department("해설단")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '해설단']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '단장', 'name': '박은주', 'baptismal_name': '비비안나', 'contact': '010-5186-7005', 'region': '더타워'},
    {'position': '부단장', 'name': '김성희', 'baptismal_name': '마리아', 'contact': '010-8890-0897', 'region': '기타'},
    {'position': '단원', 'name': '권낭경', 'baptismal_name': '젬마', 'contact': '', 'region': '에코12단지'},
    {'position': '단원', 'name': '권성철', 'baptismal_name': '안드레아', 'contact': '', 'region': '에코12단지'},
    {'position': '단원', 'name': '김은하', 'baptismal_name': '미카엘라', 'contact': '', 'region': '에코6단지'},
    {'position': '단원', 'name': '박상용', 'baptismal_name': '안드레아', 'contact': '', 'region': '에코12단지'},
    {'position': '단원', 'name': '신미경', 'baptismal_name': '스콜라스티카', 'contact': '', 'region': '기타'},
    {'position': '단원', 'name': '유지희', 'baptismal_name': '피엔시아', 'contact': '', 'region': '에코6단지'},
    {'position': '단원', 'name': '이경영', 'baptismal_name': '율리안나', 'contact': '', 'region': '소래구역'},
    {'position': '단원', 'name': '이승언', 'baptismal_name': '글라라', 'contact': '', 'region': '풍림'},
    {'position': '단원', 'name': '조은정', 'baptismal_name': '글라라', 'contact': '', 'region': '유호'},
    {'position': '단원', 'name': '진미경', 'baptismal_name': '안나', 'contact': '', 'region': '풍림'},
    {'position': '단원', 'name': '호미선', 'baptismal_name': '율리안나', 'contact': '', 'region': '풍림'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

print("\n=== 저장 완료 ===")
print(f"단체: 해설단")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: 0건 (예산 정보 없음)")
