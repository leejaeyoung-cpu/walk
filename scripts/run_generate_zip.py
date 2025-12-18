import sys
import os

# 상위 디렉토리를 path에 추가하여 utils 모듈을 찾을 수 있게 함
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.report_generator import generate_all_reports_zip

if __name__ == "__main__":
    print("🚀 전체 보고서 생성 시작...")
    try:
        zip_path = generate_all_reports_zip(2026)
        print(f"✅ 생성 완료: {zip_path}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
