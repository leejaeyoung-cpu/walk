import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 사회복지분과 생성 또는 가져오기
dept_id = create_department("사회복지분과")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '사회복지분과']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터
members_data = [
    {'position': '분과장', 'name': '육은숙', 'baptismal_name': '아네스', 'contact': '010-2443-8152', 'region': ''}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (이미지 기반 전사, 원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': 1, 'day': 7, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 1, 'day': 9, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 1, 'day': 25, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 2, 'day': 4, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 2, 'day': 13, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 2, 'day': 14, 'weekday': '토', 'event_name': '설날 선물전달(50가구)', 'church_subsidy': 3500, 'self_funded': 0, 'total': 3500},
    {'month': 2, 'day': 22, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 3, 'day': 4, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 3, 'day': 13, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 3, 'day': 25, 'weekday': '수', 'event_name': '노인대학 입학식', 'church_subsidy': 800, 'self_funded': 0, 'total': 800},
    {'month': 3, 'day': 29, 'weekday': '', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 4, 'day': 8, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 4, 'day': 10, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 4, 'day': 12, 'weekday': '일', 'event_name': '사회복지분과 바자회 음식판매', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 4, 'day': 26, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 4, 'day': 29, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 5, 'day': 2, 'weekday': '토', 'event_name': '1부모 1가정 어린이날 어린이 선물전달(50가구)', 'church_subsidy': 750, 'self_funded': 0, 'total': 750},
    {'month': 5, 'day': 6, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 5, 'day': 15, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 5, 'day': 27, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 5, 'day': 31, 'weekday': '일', 'event_name': '사회복지분과 피정', 'church_subsidy': 300, 'self_funded': 0, 'total': 300},
    {'month': 6, 'day': 5, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 6, 'day': 24, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 6, 'day': 28, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 7, 'day': 8, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 7, 'day': 10, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 7, 'day': 26, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 7, 'day': 29, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 8, 'day': 5, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 8, 'day': 14, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 8, 'day': 30, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 9, 'day': 3, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 9, 'day': 11, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 9, 'day': 19, 'weekday': '토', 'event_name': '추석선물 전달(50가구)', 'church_subsidy': 3500, 'self_funded': 0, 'total': 3500},
    {'month': 9, 'day': 20, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 9, 'day': 30, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 10, 'day': 7, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 10, 'day': 16, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 10, 'day': 18, 'weekday': '일', 'event_name': '사회복지분과 음식판매', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 10, 'day': 25, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 10, 'day': 28, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 11, 'day': 4, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 11, 'day': 13, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 11, 'day': 25, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 11, 'day': 29, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 12, 'day': 2, 'weekday': '수', 'event_name': '남동지구모임', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 12, 'day': 5, 'weekday': '금', 'event_name': '보육원 선물전달', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000},
    {'month': 12, 'day': 11, 'weekday': '금', 'event_name': '생활필수품 및 현금지원 10가구', 'church_subsidy': 2000, 'self_funded': 0, 'total': 2000},
    {'month': 12, 'day': 20, 'weekday': '일', 'event_name': '후원 감사인사 전달', 'church_subsidy': 0, 'self_funded': 0, 'total': 0},
    {'month': 12, 'day': 27, 'weekday': '일', 'event_name': '사회복지분과 월례회의(인당1만원)', 'church_subsidy': 0, 'self_funded': 10, 'total': 10},
    {'month': 12, 'day': 30, 'weekday': '수', 'event_name': '노인대학 교양강좌', 'church_subsidy': 1000, 'self_funded': 0, 'total': 1000}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 사회복지분과")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
