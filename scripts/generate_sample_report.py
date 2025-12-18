import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.report_generator import generate_dept_report

def generate_sample():
    dept_name = "사회복지분과"
    year = 2026
    save_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Project root
    
    print(f"Generating sample report for {dept_name}...")
    if generate_dept_report(dept_name, year, save_dir):
        print(f"✅ Successfully generated: {dept_name}_{year}_report.png")
    else:
        print("❌ Failed to generate report.")

if __name__ == "__main__":
    generate_sample()
