import re

def parse_members(text):
    """
    회원 명단 텍스트 파싱
    형식: 직위, 성명, 세례명, 연락처, 거주구역 (탭 또는 쉼표 구분, 한 줄에 1명)
    
    Args:
        text (str): 붙여넣기한 텍스트
        
    Returns:
        list[dict]: 파싱된 회원 데이터
    """
    members = []
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 탭 또는 쉼표로 분리 (탭 우선)
        if '\t' in line:
            parts = [p.strip() for p in line.split('\t')]
        else:
            parts = [p.strip() for p in line.split(',')]
        
        # 최소 5개 필드 필요
        if len(parts) >= 5:
            members.append({
                'position': parts[0],
                'name': parts[1],
                'baptismal_name': parts[2],
                'contact': parts[3],
                'region': parts[4]
            })
        elif len(parts) >= 3:
            # 최소 3개 필드만 있어도 처리 (직위, 성명, 세례명)
            members.append({
                'position': parts[0] if len(parts) > 0 else '',
                'name': parts[1] if len(parts) > 1 else '',
                'baptismal_name': parts[2] if len(parts) > 2 else '',
                'contact': parts[3] if len(parts) > 3 else '',
                'region': parts[4] if len(parts) > 4 else ''
            })
    
    return members

def parse_budgets(text):
    """
    예산 데이터 텍스트 파싱
    형식: 월, 일, 요일, 사업계획, 본당보조, 자체, 합계 (탭 또는 쉼표 구분)
    
    Args:
        text (str): 붙여넣기한 텍스트
        
    Returns:
        list[dict]: 파싱된 예산 데이터
    """
    budgets = []
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 탭 또는 쉼표로 분리 (탭 우선)
        if '\t' in line:
            parts = [p.strip() for p in line.split('\t')]
        else:
            parts = [p.strip() for p in line.split(',')]
        
        # 최소 7개 필드 필요
        if len(parts) >= 7:
            try:
                month = int(parts[0]) if parts[0] else None
                day = int(parts[1]) if parts[1] else None
                weekday = parts[2]
                event_name = parts[3]
                
                # 숫자에서 쉼표 제거 후 변환
                church_subsidy = int(parts[4].replace(',', '')) if parts[4] and parts[4].replace(',', '').isdigit() else 0
                self_funded = int(parts[5].replace(',', '')) if parts[5] and parts[5].replace(',', '').isdigit() else 0
                total = int(parts[6].replace(',', '')) if parts[6] and parts[6].replace(',', '').isdigit() else 0
                
                # 합계가 없으면 자동 계산
                if total == 0:
                    total = church_subsidy + self_funded
                
                budgets.append({
                    'month': month,
                    'day': day,
                    'weekday': weekday,
                    'event_name': event_name,
                    'church_subsidy': church_subsidy,
                    'self_funded': self_funded,
                    'total': total
                })
            except (ValueError, IndexError) as e:
                # 파싱 실패한 줄은 건너뛰기
                continue
    
    return budgets

def validate_members(members_data):
    """회원 데이터 검증"""
    errors = []
    for i, member in enumerate(members_data):
        if not member.get('name'):
            errors.append(f"행 {i+1}: 성명이 누락되었습니다")
    return errors

def validate_budgets(budgets_data):
    """예산 데이터 검증"""
    errors = []
    for i, budget in enumerate(budgets_data):
        if not budget.get('event_name'):
            errors.append(f"행 {i+1}: 사업계획명이 누락되었습니다")
        if budget.get('month') and (budget['month'] < 1 or budget['month'] > 12):
            errors.append(f"행 {i+1}: 월이 올바르지 않습니다 (1-12)")
    return errors
