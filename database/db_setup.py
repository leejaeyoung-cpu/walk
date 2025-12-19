import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "church_plan.db")

def create_database():
    """데이터베이스와 테이블 생성"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # 단체 테이블
    c.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # 연간 계획 테이블
    c.execute("""
        CREATE TABLE IF NOT EXISTS annual_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_id INTEGER NOT NULL,
            year INTEGER NOT NULL,
            goals TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (department_id) REFERENCES departments(id),
            UNIQUE(department_id, year)
        )
    """)
    
    # 회원 테이블
    c.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            annual_plan_id INTEGER NOT NULL,
            position TEXT,
            name TEXT NOT NULL,
            baptismal_name TEXT,
            contact TEXT,
            region TEXT,
            FOREIGN KEY (annual_plan_id) REFERENCES annual_plans(id)
        )
    """)
    
    # 예산 테이블
    c.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            annual_plan_id INTEGER NOT NULL,
            month INTEGER,
            day INTEGER,
            weekday TEXT,
            event_name TEXT NOT NULL,
            church_subsidy INTEGER DEFAULT 0,
            self_funded INTEGER DEFAULT 0,
            total INTEGER DEFAULT 0,
            FOREIGN KEY (annual_plan_id) REFERENCES annual_plans(id)
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"✅ 데이터베이스 생성 완료: {DB_FILE}")

if __name__ == "__main__":
    create_database()
