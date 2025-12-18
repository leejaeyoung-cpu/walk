import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from PIL import Image

from database.db_setup import create_database
from database.db_utils import (
    get_all_departments, create_department, get_or_create_annual_plan,
    get_members, get_budgets, update_members_from_df, update_budgets_from_df,
    get_all_budgets_by_year, get_annual_plan_goals, update_annual_plan_goals
)

# 페이지 설정
st.set_page_config(
    page_title="성당 관리 시스템",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 스타일링
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 데이터베이스 초기화
create_database()

# 사이드바 메뉴
with st.sidebar:
    st.title("⛪ 메뉴")
    menu = st.radio(
        "이동하기", 
        ["🏠 홈", "👥 신자 관리", "👨‍👩‍👧‍👦 단체 관리", "💰 예산 집행"]
    )
    
    st.divider()
    year = st.selectbox("📅 기준 연도", [2026, 2027, 2025], index=0)

# === 1. 홈 화면 ===
if menu == "🏠 홈":
    st.markdown('<div class="main-title">성당 관리 시스템</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">주임 신부 : 박병석 요셉 신부</div>', unsafe_allow_html=True)
    
    # 이미지 로드
    img_path = "assets/church_main.jpg"
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.info("성당 사진을 assets 폴더에 넣어주세요.")

# === 2. 신자 관리 ===
elif menu == "👥 신자 관리":
    st.title("👥 전체 신자 관리")
    st.info("현재 등록된 모든 단체의 신자 명단을 통합하여 관리합니다.")
    
    # 모든 단체의 신자 데이터를 가져오는 로직 (임시로 각 단체 순회)
    depts_df = get_all_departments()
    all_members = []
    
    if not depts_df.empty:
        for _, row in depts_df.iterrows():
            dept_id = row['id']
            dept_name = row['name']
            plan_id = get_or_create_annual_plan(dept_id, year)
            members = get_members(plan_id)
            if not members.empty:
                members['소속단체'] = dept_name
                all_members.append(members)
    
    if all_members:
        combined_df = pd.concat(all_members, ignore_index=True)
        # 컬럼 순서 재배치
        cols = ['소속단체'] + [c for c in combined_df.columns if c != '소속단체']
        combined_df = combined_df[cols]
        
        st.dataframe(combined_df, use_container_width=True, hide_index=True)
        st.success(f"총 {len(combined_df)}명의 신자가 등록되어 있습니다.")
    else:
        st.warning("등록된 신자 데이터가 없습니다.")

# === 3. 단체 관리 ===
elif menu == "👨‍👩‍👧‍👦 단체 관리":
    st.title("👨‍👩‍👧‍👦 단체별 관리")
    
    depts_df = get_all_departments()
    dept_names = depts_df['name'].tolist() if not depts_df.empty else []
    
    col_sel, col_add = st.columns([3, 1])
    with col_sel:
        selected_dept_name = st.selectbox("관리할 단체를 선택하세요", dept_names)
    
    if selected_dept_name:
        dept_row = depts_df[depts_df['name'] == selected_dept_name].iloc[0]
        dept_id = int(dept_row['id'])
        plan_id = get_or_create_annual_plan(dept_id, year)
        
        # 탭 구성
        tab1, tab2, tab3, tab4 = st.tabs(["🎯 연간 목표", "📋 단원 명단", "💰 예산 내역", "📊 시각화"])
        
        # 1. 연간 목표
        with tab1:
            st.subheader(f"{year}년도 {selected_dept_name} 목표")
            current_goals = get_annual_plan_goals(plan_id)
            new_goals = st.text_area(
                "한 해 동안의 목표를 입력하세요", 
                value=current_goals, 
                height=300,
                placeholder="- 예시: 전 신자 성경 필사 운동\n- 예시: 쉬는 교우 찾기 캠페인"
            )
            if st.button("목표 저장", type="primary"):
                update_annual_plan_goals(plan_id, new_goals)
                st.success("목표가 저장되었습니다!")
        
        # 2. 단원 명단
        with tab2:
            st.subheader("단원 명단 관리")
            members_df = get_members(plan_id)
            edited_members = st.data_editor(
                members_df,
                num_rows="dynamic",
                use_container_width=True,
                hide_index=True,
                key="member_editor"
            )
            if st.button("명단 저장", type="primary"):
                update_members_from_df(plan_id, edited_members)
                st.success("명단이 저장되었습니다!")
        
        # 3. 예산 내역
        with tab3:
            st.subheader("예산 계획 관리")
            budgets_df = get_budgets(plan_id)
            
            budget_config = {
                "월": st.column_config.NumberColumn("월", min_value=1, max_value=12, format="%d월"),
                "본당보조": st.column_config.NumberColumn("본당보조", format="%d"),
                "자체": st.column_config.NumberColumn("자체", format="%d"),
                "계": st.column_config.NumberColumn("계", format="%d", disabled=True),
            }
            
            edited_budgets = st.data_editor(
                budgets_df,
                num_rows="dynamic",
                use_container_width=True,
                hide_index=True,
                column_config=budget_config,
                key="budget_editor"
            )
            
            # 자동 합계 계산 (저장 전)
            edited_budgets['계'] = edited_budgets['본당보조'].fillna(0) + edited_budgets['자체'].fillna(0)
            
            if st.button("예산 저장", type="primary"):
                update_budgets_from_df(plan_id, edited_budgets)
                st.success("예산이 저장되었습니다!")
        
        # 4. 시각화 (단체별)
        with tab4:
            st.subheader(f"{selected_dept_name} 예산 분석")
            budgets_df = get_budgets(plan_id)
            
            if not budgets_df.empty:
                # 월별 흐름
                monthly_sum = budgets_df.groupby('월')['계'].sum().reset_index()
                fig_line = px.line(
                    monthly_sum, x='월', y='계', markers=True, 
                    title="월별 예산 흐름", labels={'계': '금액(천원)'}
                )
                st.plotly_chart(fig_line, use_container_width=True)
                
                # 항목별 비중
                fig_pie = px.pie(
                    budgets_df, values='계', names='사업내용', 
                    title="사업별 예산 비중"
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("예산 데이터가 없습니다.")

# === 4. 예산 집행 ===
elif menu == "💰 예산 집행":
    st.title("💰 전체 예산 집행 분석")
    
    all_budgets = get_all_budgets_by_year(year)
    
    if not all_budgets.empty:
        # KPI
        total = all_budgets['total'].sum()
        subsidy = all_budgets['church_subsidy'].sum()
        self_fund = all_budgets['self_funded'].sum()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("총 예산", f"{total:,.0f} 천원")
        c2.metric("본당 지원금", f"{subsidy:,.0f} 천원")
        c3.metric("자체 조달금", f"{self_fund:,.0f} 천원")
        
        st.divider()
        
        # 1. 분과별 비교 (Bar Chart)
        st.subheader("분과별 예산 비교")
        dept_sum = all_budgets.groupby('department')[['church_subsidy', 'self_funded']].sum().reset_index()
        dept_sum['total'] = dept_sum['church_subsidy'] + dept_sum['self_funded']
        dept_sum = dept_sum.sort_values('total', ascending=False)
        
        fig_bar = px.bar(
            dept_sum, 
            x='department', 
            y=['church_subsidy', 'self_funded'],
            title="분과별 예산 구성 (보조 vs 자체)",
            labels={'value': '금액(천원)', 'department': '분과', 'variable': '재원'},
            barmode='stack'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # 2. 월별 전체 흐름 (Line Chart)
        st.subheader("월별 전체 예산 흐름")
        monthly_total = all_budgets.groupby('month')['total'].sum().reset_index()
        fig_trend = px.line(
            monthly_total, x='month', y='total', markers=True,
            title="월별 총 지출 계획",
            labels={'total': '금액(천원)', 'month': '월'}
        )
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # 3. 전체 예산 비중 (Sunburst)
        st.subheader("전체 예산 구조 상세")
        fig_sun = px.sunburst(
            all_budgets,
            path=['department', 'event_name'],
            values='total',
            title="분과 및 사업별 예산 구조"
        )
        st.plotly_chart(fig_sun, use_container_width=True)
        
    else:
        st.info("등록된 예산 데이터가 없습니다.")
