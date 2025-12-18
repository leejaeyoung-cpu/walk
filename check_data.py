import pandas as pd
import os

# 현재 디렉토리의 모든 파일 확인
print("=== 현재 폴더의 파일 목록 ===")
for f in os.listdir('.'):
    print(f"  - {f}")

print("\n=== Excel 파일 분석 ===\n")

# Excel 파일들 확인
excel_files = [
    '2026년도 사업계획서.xlsx',
    '26년연령회사업계획.xlsx'
]

for file in excel_files:
    if os.path.exists(file):
        print(f"\n📊 {file}")
        print("-" * 80)
        try:
            xls = pd.ExcelFile(file)
            print(f"시트 목록: {xls.sheet_names}\n")
            
            # 각 시트의 데이터 미리보기
            for sheet in xls.sheet_names:
                print(f"\n>>> 시트: {sheet}")
                df = pd.read_excel(file, sheet_name=sheet)
                print(f"행 수: {len(df)}, 열 수: {len(df.columns)}")
                print(f"열 이름: {df.columns.tolist()}")
                print("\n첫 3행:")
                print(df.head(3).to_string())
                print()
        except Exception as e:
            print(f"❌ 에러: {e}")
    else:
        print(f"❌ {file} 파일을 찾을 수 없습니다.")
