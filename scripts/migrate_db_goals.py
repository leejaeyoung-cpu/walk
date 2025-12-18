import sqlite3
import os

DB_FILE = "church_plan.db"

def migrate_db():
    if not os.path.exists(DB_FILE):
        print("데이터베이스 파일이 없습니다.")
        return

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    try:
        # goals 컬럼 추가 시도
        c.execute("ALTER TABLE annual_plans ADD COLUMN goals TEXT")
        print("✅ 'goals' 컬럼이 annual_plans 테이블에 추가되었습니다.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("ℹ️ 'goals' 컬럼이 이미 존재합니다.")
        else:
            print(f"❌ 오류 발생: {e}")
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_db()
