import sys
import os

# 부모 디렉토리를 경로에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from database.db_utils import create_department, get_or_create_annual_plan, save_members, save_budgets

# 연령회 생성 또는 가져오기
dept_id = create_department("연령회")
if not dept_id:
    # 이미 존재하면 ID 가져오기
    from database.db_utils import get_all_departments
    depts = get_all_departments()
    dept_id = int(depts[depts['name'] == '연령회']['id'].values[0])

print(f"단체 ID: {dept_id}")

# 연간 계획 생성
plan_id = get_or_create_annual_plan(dept_id, 2026)
print(f"연간 계획 ID: {plan_id}")

# 명단 데이터 (이미지 기반 전사)
members_data = [
    {'position': '회원', 'name': '고정자', 'baptismal_name': '마리아', 'contact': '010-7666-1357', 'region': ''},
    {'position': '회원', 'name': '구설희', 'baptismal_name': '아우구스띠나', 'contact': '010-5045-4000', 'region': ''},
    {'position': '회원', 'name': '김경순', 'baptismal_name': '세실리아', 'contact': '010-2759-0732', 'region': ''},
    {'position': '회원', 'name': '김군이', 'baptismal_name': '로사', 'contact': '010-6414-5350', 'region': ''},
    {'position': '회원', 'name': '김말자', 'baptismal_name': '아녜스', 'contact': '010-6569-9066', 'region': ''},
    {'position': '회원', 'name': '김명순', 'baptismal_name': '데레사', 'contact': '010-8992-6294', 'region': ''},
    {'position': '회원', 'name': '김명일', 'baptismal_name': '불다', 'contact': '010-6663-6132', 'region': ''},
    {'position': '회원', 'name': '김명자', 'baptismal_name': '타티아나', 'contact': '010-2218-4995', 'region': ''},
    {'position': '회원', 'name': '김서영', 'baptismal_name': '베드로', 'contact': '', 'region': ''},
    {'position': '회원', 'name': '김수정', 'baptismal_name': '후리나', 'contact': '010-6462-1600', 'region': ''},
    {'position': '회원', 'name': '김순녀', 'baptismal_name': '루시아', 'contact': '010-2255-7722', 'region': ''},
    {'position': '회원', 'name': '김애자', 'baptismal_name': '율리안나', 'contact': '010-5463-2282', 'region': ''},
    {'position': '회원', 'name': '김영자', 'baptismal_name': '엘리사벳', 'contact': '010-8554-0883', 'region': ''},
    {'position': '회원', 'name': '김영철', 'baptismal_name': '미카엘', 'contact': '010-3738-6484', 'region': ''},
    {'position': '회원', 'name': '김영희', 'baptismal_name': '크리스티나', 'contact': '010-5412-1445', 'region': ''},
    {'position': '회원', 'name': '김연숙', 'baptismal_name': '마리아막달레나', 'contact': '010-6310-0403', 'region': ''},
    {'position': '회원', 'name': '김연옥', 'baptismal_name': '리디아', 'contact': '010-2305-0330', 'region': ''},
    {'position': '회원', 'name': '김정선', 'baptismal_name': '미카엘라', 'contact': '010-9995-6125', 'region': ''},
    {'position': '회원', 'name': '김정희', 'baptismal_name': '안나', 'contact': '010-2948-2808', 'region': ''},
    {'position': '회원', 'name': '김질순', 'baptismal_name': '마리아', 'contact': '010-5500-3057', 'region': ''},
    {'position': '회원', 'name': '김현주', 'baptismal_name': '고르다', 'contact': '010-9159-0886', 'region': ''},
    {'position': '회원', 'name': '김희자', 'baptismal_name': '릿다', 'contact': '010-4329-8395', 'region': ''},
    {'position': '회원', 'name': '노수자', 'baptismal_name': '엘리사벳', 'contact': '010-9980-1885', 'region': ''},
    {'position': '회원', 'name': '노숙자', 'baptismal_name': '엘리사벳', 'contact': '010-3400-3694', 'region': ''},
    {'position': '회원', 'name': '노순하', 'baptismal_name': '데레사', 'contact': '010-4909-9119', 'region': ''},
    {'position': '회원', 'name': '마이금', 'baptismal_name': '미카엘라', 'contact': '010-3949-1030', 'region': ''},
    {'position': '회원', 'name': '문애익', 'baptismal_name': '엘리사벳', 'contact': '010-2004-2999', 'region': ''},
    {'position': '회원', 'name': '문상후', 'baptismal_name': '다니엘', 'contact': '010-5410-1440', 'region': ''},
    {'position': '회원', 'name': '문인순', 'baptismal_name': '데레사', 'contact': '010-3352-0400', 'region': ''},
    {'position': '회원', 'name': '민규철', 'baptismal_name': '리디아', 'contact': '010-2566-6035', 'region': ''},
    {'position': '회원', 'name': '박갑수', 'baptismal_name': '바오로', 'contact': '010-3300-3025', 'region': ''},
    {'position': '회원', 'name': '박광서', 'baptismal_name': '루카', 'contact': '010-2757-1401', 'region': ''},
    {'position': '회원', 'name': '박규철', 'baptismal_name': '요한', 'contact': '010-3949-1030', 'region': ''},
    {'position': '회원', 'name': '박남순', 'baptismal_name': '안나', 'contact': '010-2505-1281', 'region': ''},
    {'position': '회원', 'name': '박성자', 'baptismal_name': '작은안나', 'contact': '010-3760-1303', 'region': ''},
    {'position': '회원', 'name': '박승일', 'baptismal_name': '베드로', 'contact': '010-6239-4561', 'region': ''},
    {'position': '회원', 'name': '박연수', 'baptismal_name': '스테파노', 'contact': '010-3245-5960', 'region': ''},
    {'position': '회원', 'name': '박태수', 'baptismal_name': '베로니카', 'contact': '010-5522-4165', 'region': ''},
    {'position': '회원', 'name': '배준혁', 'baptismal_name': '미카엘', 'contact': '010-2209-0110', 'region': ''},
    {'position': '회원', 'name': '백덕이', 'baptismal_name': '수산나', 'contact': '010-3333-5157', 'region': ''},
    {'position': '회원', 'name': '백정숙', 'baptismal_name': '사비나', 'contact': '010-4528-4441', 'region': ''},
    {'position': '회원', 'name': '서경자', 'baptismal_name': '비비안나', 'contact': '010-3133-0455', 'region': ''},
    {'position': '회원', 'name': '서영복', 'baptismal_name': '프란치스코', 'contact': '010-2444-5014', 'region': ''},
    {'position': '회원', 'name': '성기남', 'baptismal_name': '요셉', 'contact': '010-3321-4958', 'region': ''},
    {'position': '회원', 'name': '신관실', 'baptismal_name': '사라', 'contact': '010-5761-3461', 'region': ''},
    {'position': '회원', 'name': '심길섭', 'baptismal_name': '마르타', 'contact': '010-3200-5966', 'region': ''},
    {'position': '회원', 'name': '양은분', 'baptismal_name': '세실리아', 'contact': '010-3334-5414', 'region': ''},
    {'position': '회원', 'name': '엄미경', 'baptismal_name': '안나', 'contact': '010-3079-4791', 'region': ''},
    {'position': '회원', 'name': '오금순', 'baptismal_name': '모니카', 'contact': '010-5382-1664', 'region': ''},
    {'position': '회원', 'name': '오옥자', 'baptismal_name': '데레사', 'contact': '010-3354-5594', 'region': ''},
    {'position': '회원', 'name': '유경자', 'baptismal_name': '안나', 'contact': '010-5336-1631', 'region': ''},
    {'position': '회원', 'name': '유수종', 'baptismal_name': '세바스티아노', 'contact': '010-5415-1341', 'region': ''},
    {'position': '회원', 'name': '유의목', 'baptismal_name': '사라', 'contact': '010-4446-0643', 'region': ''},
    {'position': '회원', 'name': '유정은', 'baptismal_name': '비비안나', 'contact': '010-3924-6641', 'region': ''},
    {'position': '회원', 'name': '유정희', 'baptismal_name': '레아', 'contact': '010-8305-6035', 'region': ''},
    {'position': '회원', 'name': '유지이', 'baptismal_name': '소화데레사', 'contact': '010-2810-1094', 'region': ''},
    {'position': '회원', 'name': '유영미', 'baptismal_name': '', 'contact': '', 'region': ''},
    {'position': '회원', 'name': '이광선', 'baptismal_name': '베드로', 'contact': '010-2018-9161', 'region': ''},
    {'position': '회원', 'name': '이복자', 'baptismal_name': '베로니카', 'contact': '010-6450-1331', 'region': ''},
    {'position': '회원', 'name': '이숙영', 'baptismal_name': '논나', 'contact': '010-3391-0391', 'region': ''},
    {'position': '회원', 'name': '이순임', 'baptismal_name': '모니카', 'contact': '010-7235-4340', 'region': ''},
    {'position': '회원', 'name': '이승미', 'baptismal_name': '루치아', 'contact': '전화금지(문자)', 'region': ''},
    {'position': '회원', 'name': '이승희', 'baptismal_name': '요셉', 'contact': '010-4103-3396', 'region': ''},
    {'position': '회원', 'name': '이연숙', 'baptismal_name': '실비아', 'contact': '010-6455-0331', 'region': ''},
    {'position': '회원', 'name': '이영규', 'baptismal_name': '시몬', 'contact': '010-5405-3836', 'region': ''},
    {'position': '회원', 'name': '이윤미', 'baptismal_name': '아녜스', 'contact': '010-5516-0636', 'region': ''},
    {'position': '회원', 'name': '이인숙', 'baptismal_name': '율리안나', 'contact': '010-3320-5463', 'region': ''},
    {'position': '회원', 'name': '이재섭', 'baptismal_name': '세라', 'contact': '', 'region': ''},
    {'position': '회원', 'name': '이재영', 'baptismal_name': '엘리사벳', 'contact': '010-6409-6341', 'region': ''},
    {'position': '회원', 'name': '이정실', 'baptismal_name': '베드로', 'contact': '010-9913-7441', 'region': ''},
    {'position': '회원', 'name': '이종순', 'baptismal_name': '성령의다락방', 'contact': '032-5519-4841', 'region': ''},
    {'position': '회원', 'name': '이향은', 'baptismal_name': '모니카', 'contact': '010-4112-6991', 'region': ''},
    {'position': '회원', 'name': '임수호', 'baptismal_name': '미카엘', 'contact': '010-2925-0528', 'region': ''},
    {'position': '회원', 'name': '임애경', 'baptismal_name': '안나', 'contact': '010-3271-1837', 'region': ''},
    {'position': '회원', 'name': '임양섭', 'baptismal_name': '모니카', 'contact': '010-7374-6484', 'region': ''},
    {'position': '회원', 'name': '임춘희', 'baptismal_name': '리디안나', 'contact': '010-3354-4358', 'region': ''},
    {'position': '회원', 'name': '장순기', 'baptismal_name': '세실리아', 'contact': '010-6321-2910', 'region': ''},
    {'position': '회원', 'name': '장태숙', 'baptismal_name': '아가타', 'contact': '010-3554-4844', 'region': ''},
    {'position': '회원', 'name': '전대영', 'baptismal_name': '요세피나', 'contact': '010-7200-3394', 'region': ''},
    {'position': '회원', 'name': '전영미', 'baptismal_name': '율리안나', 'contact': '010-4336-7676', 'region': ''},
    {'position': '회원', 'name': '정구순', 'baptismal_name': '알로이시아', 'contact': '010-8924-0220', 'region': ''},
    {'position': '회원', 'name': '정규실', 'baptismal_name': '야고보', 'contact': '010-0000-7404', 'region': ''},
    {'position': '회원', 'name': '정명자', 'baptismal_name': '클라라', 'contact': '010-3441-8230', 'region': ''},
    {'position': '회원', 'name': '정선택', 'baptismal_name': '다니엘', 'contact': '010-5333-0004', 'region': ''},
    {'position': '회원', 'name': '정영교', 'baptismal_name': '제오르지오', 'contact': '010-3859-6184', 'region': ''},
    {'position': '회원', 'name': '정옥분', 'baptismal_name': '안나', 'contact': '010-2243-6600', 'region': ''},
    {'position': '회원', 'name': '정윤원', 'baptismal_name': '미카엘', 'contact': '010-5209-0248', 'region': ''},
    {'position': '회원', 'name': '조미경', 'baptismal_name': '데레사', 'contact': '010-5882-8888', 'region': ''},
    {'position': '회원', 'name': '조의심', 'baptismal_name': '모니카', 'contact': '010-3400-0155', 'region': ''},
    {'position': '회원', 'name': '조원진', 'baptismal_name': '사도요한', 'contact': '010-5500-1037', 'region': ''},
    {'position': '회원', 'name': '천화순', 'baptismal_name': '데레사', 'contact': '010-5258-1844', 'region': ''},
    {'position': '회원', 'name': '최국화', 'baptismal_name': '글로리아', 'contact': '010-3342-4311', 'region': ''},
    {'position': '회원', 'name': '최영물', 'baptismal_name': '데레사', 'contact': '010-4505-6059', 'region': ''},
    {'position': '회원', 'name': '최정수', 'baptismal_name': '루카', 'contact': '010-3788-4232', 'region': ''},
    {'position': '회원', 'name': '최준희', 'baptismal_name': '아가다', 'contact': '010-3327-0050', 'region': ''},
    {'position': '회원', 'name': '하영실', 'baptismal_name': '스텔라', 'contact': '010-9259-9667', 'region': ''},
    {'position': '회원', 'name': '한임상', 'baptismal_name': '호안나', 'contact': '010-6333-1041', 'region': ''},
    {'position': '회원', 'name': '함병루', 'baptismal_name': '세실리아', 'contact': '010-2215-4560', 'region': ''},
    {'position': '회원', 'name': '허상', 'baptismal_name': '안토니오', 'contact': '010-6400-6504', 'region': ''},
    {'position': '회원', 'name': '황경아', 'baptismal_name': '세실리아', 'contact': '010-5191-4029', 'region': ''},
    {'position': '회원', 'name': '황치성', 'baptismal_name': '베드로', 'contact': '010-6788-3774', 'region': ''}
]

# 명단 저장
member_count = save_members(plan_id, members_data)
print(f"✅ 명단 저장 완료: {member_count}명")

# 예산 데이터 (원 단위를 천원 단위로 변환)
budgets_data = [
    {'month': 1, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 2, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 3, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 4, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 6, 'day': None, 'weekday': '', 'event_name': '회합 후 중식제공', 'church_subsidy': 100, 'self_funded': 360, 'total': 460},
    {'month': 7, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 8, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 9, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 10, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 12, 'day': None, 'weekday': '', 'event_name': '회합 시 간식', 'church_subsidy': 100, 'self_funded': 50, 'total': 150},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '남동지구연합회 회비', 'church_subsidy': 100, 'self_funded': 0, 'total': 100},
    {'month': 5, 'day': None, 'weekday': '', 'event_name': '교구 연합회 회비', 'church_subsidy': 120, 'self_funded': 0, 'total': 120},
    {'month': 11, 'day': None, 'weekday': '', 'event_name': '위령의날 백석 묘지', 'church_subsidy': 700, 'self_funded': 950, 'total': 1650}
]

# 예산 저장
budget_count = save_budgets(plan_id, budgets_data)
print(f"✅ 예산 저장 완료: {budget_count}건")

print("\n=== 저장 완료 ===")
print(f"단체: 연령회")
print(f"년도: 2026")
print(f"명단: {member_count}명")
print(f"예산: {budget_count}건")
