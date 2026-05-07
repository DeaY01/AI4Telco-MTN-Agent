import streamlit as st
import pandas as pd
from ai_core import run_success_logic

st.set_page_config(layout="wide", page_title="MTN Agent Workspace")

# MTN PROFESSIONAL DESIGN SYSTEM
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .mtn-header { 
        background-color: #FFCC00; 
        padding: 20px; 
        border-bottom: 8px solid #000; 
        display:flex; 
        justify-content:space-between; 
        align-items:center; 
    }
    .mtn-logo { background-color: #000; color: #FFCC00; padding: 8px 15px; font-weight: 900; border-radius: 4px; }
    .case-card { 
        border: 1px solid #E0E0E0; 
        padding: 12px; 
        border-radius: 4px; 
        margin-bottom: 8px; 
    }
    .case-card:hover { border-color: #000; background-color: #F9F9F9; }
    .nba-highlight { 
        background-color: #000; 
        color: #FFCC00; 
        padding: 15px; 
        border-radius: 4px; 
        font-weight: bold;
    }
    .status-badge {
        font-size: 0.65rem;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        text-transform: uppercase;
        color: #FFF;
    }
    </style>
    <div class='mtn-header'>
        <h1 style='color:#000; margin:0;'>FRONTLINE AGENT WORKSPACE</h1>
        <div class='mtn-logo'>MTN</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# Layout: Simple Queue (Left) and Workspace (Right)
col_q, col_w = st.columns([1, 2.5], gap="large")

with col_q:
    st.subheader("Unified Queue")
    
    # CATEGORICAL PRIORITY MATRIX (One-click filtering)
    # Replaces the slider for faster operational use
    st.write("Filter by Priority:")
    c1, c2, c3, c4, c5 = st.columns(5)
    
    if 'filter' not in st.session_state:
        st.session_state.filter = "All"

    if c1.button("All", use_container_width=True): st.session_state.filter = "All"
    if c2.button("Critical", use_container_width=True): st.session_state.filter = "Critical"
    if c3.button("High", use_container_width=True): st.session_state.filter = "High"
    if c4.button("Med", use_container_width=True): st.session_state.filter = "Medium"
    if c5.button("Low", use_container_width=True): st.session_state.filter = "Low"

    st.markdown(f"**Viewing: {st.session_state.filter} Priority Cases**")

    # 12 SAMPLES: Structured for MTN Business Verticals
    queue_data = [
        {"id": "SR-9021", "name": "Alhaji Musa", "priority": "Critical", "cat": "Data Services", "time": "2m"},
        {"id": "SR-8842", "name": "Bayo Ade", "priority": "High", "cat": "Network Infra", "time": "5m"},
        {"id": "SR-7731", "name": "Chioma O.", "priority": "Medium", "cat": "Revenue/Billing", "time": "14m"},
        {"id": "SR-6620", "name": "Emeka J.", "priority": "Low", "cat": "General Inquiry", "time": "45m"},
        {"id": "SR-5511", "name": "Fatima B.", "priority": "Critical", "cat": "MoMo/Fintech", "time": "1m"},
        {"id": "SR-4402", "name": "Ibrahim K.", "priority": "High", "cat": "Roaming", "time": "8m"},
        {"id": "SR-3391", "name": "Joy U.", "priority": "Medium", "cat": "Data Services", "time": "20m"},
        {"id": "SR-2280", "name": "Kelechi P.", "priority": "Low", "cat": "VAS Subscription", "time": "1h"},
        {"id": "SR-1175", "name": "Mustafa R.", "priority": "Critical", "cat": "Network Infra", "time": "3m"},
        {"id": "SR-0064", "name": "Ngozi S.", "priority": "High", "cat": "Revenue/Billing", "time": "10m"},
        {"id": "SR-9953", "name": "Olumide W.", "priority": "Medium", "cat": "MoMo/Fintech", "time": "30m"},
        {"id": "SR-8841", "name": "Patience E.", "priority": "Low", "cat": "SIM Services", "time": "2h"}
    ]
    
    # Filter logic
    f_type = st.session_state.filter
    filtered_data = [d for d in queue_data if f_type == "All" or d['priority'] == f_type]
    
    for item in filtered_data:
        p_map = {"Critical": "#000000", "High": "#D32F2F", "Medium": "#666666", "Low": "#9E9E9E"}
        p_color = p_map.get(item['priority'], "#666")
        
        with st.container():
            st.markdown(f"""
                <div class='case-card'>
                    <div style='display:flex; justify-content:space-between;'>
                        <small>{item['id']}</small>
                        <small>{item['time']}</small>
                    </div>
                    <strong>{item['name']}</strong><br>
                    <span class='status-badge' style='background:{p_color};'>{item['priority']}</span>
                    <span style='font-size: 0.75rem; color:#666;'> | {item['cat']}</span>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Analyze {item['id']}", key=item['id'], use_container_width=True):
                st.session_state.active_case = item

with col_w:
    if 'active_case' in st.session_state:
        case = st.session_state.active_case
        st.subheader(f"Workspace: {case['name']} - {case['priority']}")
        
        input_text = st.text_area("Interaction Feed", height=100, 
                                  placeholder="Live transcript from USSD, Twitter, or Voice...")
        
        if st.button("EXECUTE SUCCESS AI ANALYSIS", use_container_width=True):
            st.session_state.result = run_success_logic(input_text)

        if 'result' in st.session_state:
            res = st.session_state.result
            
            st.write("---")
            st.markdown("### Decision Support")
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Customer Experience (CX)**")
                risk_lvl = 95 if case['priority'] == "Critical" else 70 if case['priority'] == "High" else 30
                st.progress(risk_lvl)
                st.caption(f"Risk of Churn: {case['priority']}")
            with c2:
                st.write("**Business Intelligence (BI)**")
                st.progress(20)
                st.caption("Revenue Integrity: Verified")

            st.markdown("#### Next Best Action (NBA)")
            st.markdown(f"<div class='nba-highlight'>{res['nba']}</div>", unsafe_allow_html=True)
            
            st.write("")
            st.markdown("**AI Recommended Response Script**")
            st.code(f"Hello {case['name'].split()[0]}, I have analyzed your {case['cat']} logs. Based on the {case['priority']} priority flag, I have initiated {res['nba']}.")
            
            act1, act2 = st.columns(2)
            act1.button("Resolve Case", use_container_width=True)
            act2.button("Escalate", use_container_width=True)
    else:
        st.info("Select a case from the priority-filtered queue to begin.")

st.divider()
st.caption("SUCCESS Team Framework | Priority Matrix Governance | CX-BI Decision Alignment")