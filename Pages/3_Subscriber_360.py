import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="MTN Recovery Hub")

# MTN ENTERPRISE DESIGN
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .mtn-header { 
        background-color: #FFCC00; padding: 20px; border-bottom: 8px solid #000; 
        display:flex; justify-content:space-between; align-items:center; 
    }
    .mtn-logo { background-color: #000; color: #FFCC00; padding: 8px 15px; font-weight: 900; border-radius: 4px; }
    .logic-box { 
        background-color: #F8F9FA; border-left: 5px solid #000; 
        padding: 15px; margin-bottom: 20px; 
    }
    .recovery-action { background-color: #000; color: #FFCC00; padding: 20px; border-radius: 4px; }
    </style>
    <div class='mtn-header'>
        <h1 style='color:#000; margin:0;'>SUBSCRIBER 360 RECOVERY HUB</h1>
        <div class='mtn-logo'>MTN</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# 1. SUBSCRIBER LOOKUP
col_s, _ = st.columns([2, 2])
msisdn = col_s.text_input("Search Subscriber MSISDN:", placeholder="234803...")

if msisdn:
    # 2. BUSINESS INTELLIGENCE LAYER (Slide 01 & 02)
    st.subheader(f"Account Integrity: {msisdn}")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Customer Value", "Platinum")
    m2.metric("Churn Risk Score", "84%", "Critical")
    m3.metric("Last 7D Spend", "₦12,400")
    m4.metric("Verified Outages", "3 Events")

    st.divider()

    # 3. TECHNICAL-COMMERCIAL CORRELATION (Innovation)
    st.write("### Data-to-Problem Mapping")
    st.caption("Correlating Network CDR Signals with Billing Anomalies")
    
    col_chart, col_rules = st.columns([2, 1])

    with col_chart:
        # Visualizing the "Evidence" for recovery
        # FIX APPLIED: freq='h' instead of freq='H'
        chart_data = pd.DataFrame({
            "Time": pd.date_range("2024-05-01", periods=10, freq="h"),
            "Signal_Strength": [90, 88, 30, 25, 20, 85, 90, 92, 88, 90],
            "Data_Consumption": [400, 380, 10, 5, 2, 410, 450, 430, 400, 410]
        })
        st.line_chart(chart_data, x="Time", y=["Signal_Strength", "Data_Consumption"], color=["#000000", "#FFCC00"])

    with col_rules:
        # 4. BUSINESS LOGIC GATEWAY (Slide 06 Governance)
        st.write("**Governance Logic**")
        st.markdown("""
            <div class='logic-box'>
                <small>RULE_ID: RET-402</small><br>
                <strong>STATUS: PRE-APPROVED</strong><br><br>
                <small>LOGIC APPLIED:</small><br>
                <span>IF Signal < -85dBm AND Value == Platinum THEN Trigger Recovery</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Explainable AI (XAI) - Slide 07
        st.info("AI Logic: 84% Churn probability is driven by 3 consecutive data session timeouts during peak business hours.")

    st.divider()

    # 5. THE RECOVERY ENGINE
    st.write("### Execute Revenue Recovery")
    
    rec_l, rec_r = st.columns(2)
    
    with rec_l:
        st.markdown("""
            <div class='recovery-action'>
                <small>RECOMMENDED ACTION</small>
                <h2 style='color:#FFCC00; margin:0;'>2GB Integrity Refund</h2>
                <p style='font-size:0.85rem;'>Automated gesture to compensate for verified network downtime.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Apply Pre-Approved Refund", use_container_width=True):
            st.success("Refund Processed. Audit Log Updated: RULE_RET-402_EXEC")

    with rec_r:
        st.write("**Alternative Retention Options**")
        st.checkbox("Priority Network Access (Turbo Mode)")
        st.checkbox("₦500 MoMo Airtime Voucher")
        st.checkbox("Waive Next Subscription Charge")
        st.button("Manual Override & Escalate", use_container_width=True)

else:
    st.info("Enter an MSISDN to load the 360-degree recovery profile.")

# FOOTER
st.divider()
st.caption("SUCCESS Team Framework | Business Rules Logic Layer | Revenue Integrity & Compliance View")