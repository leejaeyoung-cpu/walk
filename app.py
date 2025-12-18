import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database.db_setup import create_database
from database.db_utils import (
    get_all_departments, create_department, get_or_create_annual_plan,
    get_members, get_budgets, update_members_from_df, update_budgets_from_df,
    get_all_budgets_by_year
)

# 페이지 설정 (반드시 최상단)
st.set_page_config(
    page_title="2026년 교회 사업계획 관리 시스템",
    page_icon="⛪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 스타일링 커스텀
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 데이터베이스 초기화
create_database()

# 사이드바: 네비게이션 및 설정
with st.sidebar:
    st.title("⛪ 관리 시스템")
    
    # 년도 선택
    year = st.selectbox("📅 사업 연도", [2026, 2027, 2025], index=0)
    
    st.divider()
    
    # 단체 선택
    depts_df = get_all_departments()
    dept_names = depts_df['name'].tolist() if not depts_df.empty else []
    
    selected_dept_name = st.selectbox(
        "단체 선택", 
        ["전체 현황 (Dashboard)"] + dept_names
    )
    
    # 새 단체 추가
    with st.expander("➕ 새 단체 추가"):
        new_dept_name = st.text_input("단체명 입력")
        if st.button("추가하기"):
            if new_dept_name:
                create_department(new_dept_name)
                st.success(f"'{new_dept_name}' 추가됨!")
                st.rerun()

# 메인 컨텐츠
if selected_dept_name == "전체 현황 (Dashboard)":
    st.title(f"📊 {year}년도 전체 사업계획 현황")
    
    # 전체 데이터 로드
    all_budgets = get_all_budgets_by_year(year)
    
    if not all_budgets.empty:
        # 주요 지표 (KPI)
        total_budget = all_budgets['total'].sum()
        church_subsidy = all_budgets['church_subsidy'].sum()
        self_funded = all_budgets['self_funded'].sum()
        dept_count = all_budgets['department'].nunique()
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("총 예산 (천원)", f"{total_budget:,.0f}")
        col2.metric("본당 보조 (천원)", f"{church_subsidy:,.0f}")
        col3.metric("자체 조달 (천원)", f"{self_funded:,.0f}")
        col4.metric("등록 단체 수", f"{dept_count}개")
        
        st.divider()
        
        # 차트 영역
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("단체별 예산 분포")
            fig_bar = px.bar(
                all_budgets.groupby('department')[['church_subsidy', 'self_funded']].sum().reset_index(),
                x='department', 
                y=['church_subsidy', 'self_funded'],
                title="단체별 예산 구성 (본당보조 vs 자체)",
                labels={'value': '금액 (천원)', 'department': '단체', 'variable': '구분'},
                barmode='stack'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with c2:
            st.subheader("예산 비율 (Sunburst)")
            fig_sun = px.sunburst(
                all_budgets,
                path=['department', 'event_name'],
                values='total',
                title="단체 및 사업별 예산 비중"
            )
            st.plotly_chart(fig_sun, use_container_width=True)
            
        # 월별 흐름
        st.subheader("월별 예산 지출 흐름")
        monthly_trend = all_budgets.groupby('month')['total'].sum().reset_index()
        fig_line = px.line(
            monthly_trend, 
            x='month', 
            y='total', 
            markers=True,
            title="월별 총 지출 계획",
            labels={'total': '금액 (천원)', 'month': '월'}
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
    else:
        st.info("등록된 예산 데이터가 없습니다.")

else:
    # 개별 단체 관리 페이지
    dept_row = depts_df[depts_df['name'] == selected_dept_name].iloc[0]
    dept_id = int(dept_row['id'])
    plan_id = get_or_create_annual_plan(dept_id, year)
    
    st.title(f"📑 {selected_dept_name} - {year}년 사업계획")
    
    # 3:7 비율로 화면 분할
    left_col, right_col = st.columns([3.5, 6.5])
    
    # === 좌측: 명단 및 기본 정보 ===
    with left_col:
        st.subheader("📋 임원 및 회원 명단")
        members_df = get_members(plan_id)
        
        # 데이터 에디터 설정을 위한 컬럼 매핑
        column_config = {
            "직책": st.column_config.TextColumn("직책", width="small"),
            "성명": st.column_config.TextColumn("성명", width="small"),
            "세례명": st.column_config.TextColumn("세례명", width="small"),
            "연락처": st.column_config.TextColumn("연락처", width="medium"),
            "구역": st.column_config.TextColumn("구역", width="small"),
        }
        
        # 빈 행 추가 기능이 있는 에디터
        edited_members = st.data_editor(
            members_df,
            num_rows="dynamic",
            use_container_width=True,
            hide_index=True,
            key="member_editor"
        )
        
        if st.button("💾 명단 저장", type="primary", use_container_width=True):
            if update_members_from_df(plan_id, edited_members):
                st.success("명단이 저장되었습니다!")
                st.rerun()
            else:
                st.error("저장 중 오류가 발생했습니다.")
                
        st.info(f"총 인원: {len(members_df)}명")

    # === 우측: 예산 및 시각화 ===
    with right_col:
        st.subheader("💰 예산 계획 및 내역")
        
        budgets_df = get_budgets(plan_id)
        
        # 탭으로 기능 분리
        tab1, tab2 = st.tabs(["📝 예산 편집", "📊 시각화 분석"])
        
        with tab1:
            # 예산 에디터
            budget_config = {
                "월": st.column_config.NumberColumn("월", min_value=1, max_value=12, format="%d월", width="small"),
                "일": st.column_config.NumberColumn("일", min_value=1, max_value=31, format="%d일", width="small"),
                "요일": st.column_config.SelectboxColumn("요일", options=["월", "화", "수", "목", "금", "토", "일"], width="small"),
                "사업내용": st.column_config.TextColumn("사업내용", width="large"),
                "본당보조": st.column_config.NumberColumn("본당보조", format="%d", step=1),
                "자체": st.column_config.NumberColumn("자체", format="%d", step=1),
                "계": st.column_config.NumberColumn("계", format="%d", disabled=True), # 자동 계산용이나 보여주기용
            }
            
            # 합계 자동 계산 (편집 중에는 반영 안됨, 저장 시 반영하거나 JS필요. 여기선 저장 후 재계산 방식)
            edited_budgets = st.data_editor(
                budgets_df,
                num_rows="dynamic",
                use_container_width=True,
                hide_index=True,
                column_config=budget_config,
                key="budget_editor"
            )
            
            # 자동 합계 계산 로직 (저장 전 전처리)
            edited_budgets['계'] = edited_budgets['본당보조'].fillna(0) + edited_budgets['자체'].fillna(0)
            
            col_save, col_stat = st.columns([1, 2])
            with col_save:
                if st.button("💾 예산 저장", type="primary", use_container_width=True):
                    if update_budgets_from_df(plan_id, edited_budgets):
                        st.success("예산이 저장되었습니다!")
                        st.rerun()
                    else:
                        st.error("저장 실패")
            
            with col_stat:
                total_sum = edited_budgets['계'].sum()
                st.markdown(f"**총 예산 합계: :blue[{total_sum:,.0f} 천원]**")

        with tab2:
            if not budgets_df.empty:
                # 1. 파이 차트 (보조 vs 자체)
                total_subsidy = budgets_df['본당보조'].sum()
                total_self = budgets_df['자체'].sum()
                
                fig_pie = px.pie(
                    names=['본당보조', '자체조달'],
                    values=[total_subsidy, total_self],
                    title="예산 재원 비율",
                    hole=0.4
                )
                st.plotly_chart(fig_pie, use_container_width=True)
                
                # 2. 월별 지출 막대 차트
                monthly_sum = budgets_df.groupby('월')['계'].sum().reset_index()
                fig_bar = px.bar(
                    monthly_sum,
                    x='월',
                    y='계',
                    title="월별 지출 계획",
                    labels={'계': '금액 (천원)', '월': '월'},
                    text_auto=True
                )
                st.plotly_chart(fig_bar, use_container_width=True)
                
                # 3. 사업별 비중 (트리맵)
                fig_tree = px.treemap(
                    budgets_df,
                    path=['사업내용'],
                    values='계',
                    title="사업별 예산 규모"
                )
                st.plotly_chart(fig_tree, use_container_width=True)
            else:
                st.info("예산 데이터를 입력하면 시각화가 표시됩니다.")

