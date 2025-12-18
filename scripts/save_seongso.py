import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 성소분과 생성 또는 가져오기
dept_id = create_department("성소분과")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '성소분과']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '분과장', 'name': '황민영', 'baptismal_name': '비비안나', 'contact': '010-2405-2148', 'region': '기타'},
    {'position': '활동회원', 'name': '김희자', 'baptismal_name': '릿다', 'contact': '', 'region': '유호'},
    {'position': '활동회원', 'name': '문금주', 'baptismal_name': '크리스티나', 'contact': '', 'region': '에코11'}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터
budgets_data = [
    {'month': 1, 'day': 7, 'weekday': '수', 'event_name': '사제서품식', 'church_subsidy': 2000, 'self_funded': 1000, 'total': 3000},
    {'month': 1, 'day': 11, 'weekday': '일', 'event_name': '새사제 첫 미사 및 축하연', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '2026학년도 1학기 예비신학교 등록', 'church_subsidy': 0, 'self_funded': 300, 'total': 300},
    {'month': 3, 'day': 2, 'weekday': '월', 'event_name': '직 수여식 미사', 'church_subsidy': 700, 'self_funded': 1300, 'total': 2000},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '성소주일 행사 참석(주일학교 전체 대상)', 'church_subsidy': 700, 'self_funded': 1500, 'total': 2200},
    {'month': 8, 'day': None, 'weekday': '', 'event_name': '예신학생 간담회', 'church_subsidy': 0, 'self_funded': 200, 'total': 200},
    {'month': 9, 'day': None, 'weekday': '', 'event_name': '2학기 예비신학교 등록', 'church_subsidy': 0, 'self_funded': 300, 'total': 300},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '어린이복사단 스포츠데이지원', 'church_subsidy': 0, 'self_funded': 1200, 'total': 1200},
    {'month': None, 'day': None, 'weekday': '', 'event_name': '어린이복사단 크리스마스지원', 'church_subsidy': 0, 'self_funded': 400, 'total': 400}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 성소분과")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
