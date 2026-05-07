import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

st.set_page_config(page_title="MTN SUCCESS | Live Interaction Pulse", layout="wide")

# MTN ENTERPRISE DESIGN SYSTEM
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .mtn-header { 
        background-color: #FFCC00; 
        padding: 20px; 
        border-bottom: 8px solid #000; 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
    }
    .mtn-logo { 
        background-color: #000; 
        color: #FFCC00; 
        padding: 10px 20px; 
        font-weight: 900; 
        border-radius: 4px; 
        font-family: 'Arial Black';
    }
    .live-indicator {
        color: red;
        font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0; } }
    </style>
    <div class='mtn-header'>
        <h1 style='color:#000; margin:0;'>RETENTION MANAGER: MULTI-USER LIVE PULSE</h1>
        <div class='mtn-logo'>MTN</div>
    </div>
""", unsafe_allow_html=True)

# TOP LEVEL KPI BAR
st.write("")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Active Live Streams", "14", "Real-time")
k2.metric("Mean Interaction Tension", "0.42", "Moderate")
k3.metric("Revenue at Risk (Live)", "₦1.2M", "P1 Severity")
k4.metric("Agent Sync Accuracy", "92%", "Optimal")

st.divider()

# INNOVATION: The Multi-User Selection & Pulse Trace
# This allows the Manager to "tune in" to any active session
st.subheader("📡 Global Interaction Sync Monitor")
active_sessions = ["Session_234803 (Lekki)", "Session_234814 (Ikeja)", "Session_234706 (Yaba)", "Session_234905 (Abuja)"]
selected_session = st.selectbox("Select Active Interaction to Deep-Scan:", active_sessions)

st.markdown(f"<span class='live-indicator'>● LIVE TRACING: {selected_session}</span>", unsafe_allow_html=True)

pulse_placeholder = st.empty()

# Motion logic for the demo pitch
for i in range(1, 11):
    with pulse_placeholder.container():
        t = np.linspace(0, 10, 60)
        # Session-specific noise simulation
        bias = 5 if "Lekki" in selected_session else -5
        
        # Yellow: Subscriber Sentiment | Black: Agent Next-Best-Action Alignment
        sub_wave = np.sin(t + i) * 3 + (75 + bias) 
        agent_wave = np.sin(t + i + 0.3) * 2 + (77 + bias)
        
        df_trace = pd.DataFrame({'Time': t, 'Subscriber Sentiment': sub_wave, 'Agent NBA Alignment': agent_wave})
        fig = px.line(df_trace, x='Time', y=['Subscriber Sentiment', 'Agent NBA Alignment'],
                      color_discrete_map={'Subscriber Sentiment': '#FFCC00', 'Agent NBA Alignment': '#000000'})
        
        fig.update_layout(height=350, margin=dict(l=0, r=0, t=20, b=0), legend=dict(orientation="h", y=1.1, x=1))
        st.plotly_chart(fig, use_container_width=True)
        time.sleep(0.1)

st.divider()

# THE INNOVATIVE "STATE OF INTERACTION" TABLE
# Tracks many users simultaneously for the Manager
st.subheader("👥 Live Interaction Multi-Feed")
st.caption("AI-powered classification of the current state between Agent and User.")

interaction_data = [
    {"MSISDN": "234803***1122", "Agent": "A_Jacob", "Vertical": "Data Services", "State": "Diverged", "Tension": "High", "NBA_Status": "Playbook Injected"},
    {"MSISDN": "234814***9901", "Agent": "A_Taiwo", "Vertical": "Network Infra", "State": "Synchronized", "Tension": "Low", "NBA_Status": "Auto-Closed"},
    {"MSISDN": "234706***2233", "Agent": "A_Mustapha", "Vertical": "Revenue/Billing", "State": "Recovering", "Tension": "Medium", "NBA_Status": "Manual Review"},
    {"MSISDN": "234905***8844", "Agent": "A_Patrick", "Vertical": "VAS/MoMo", "State": "High Risk", "Tension": "Critical", "NBA_Status": "Supervisor Alert"}
]

# Display as professional interactive grid
df_interact = pd.DataFrame(interaction_data)

def style_state(val):
    if val == "Diverged" or val == "High Risk": return "background-color: #000000; color: #FFCC00; font-weight: bold;"
    if val == "Synchronized": return "background-color: #FFCC00; color: #000000; font-weight: bold;"
    return ""

st.table(df_interact.style.map(style_state, subset=['State']))

# INNOVATION CONCLUSION
st.info("""
    **SUCCESS Team Innovation Insight:** This dashboard addresses the 'Siloed Data' problem by pulling real-time sentiment from the Agent Copilot. 
    A **'Diverged'** state warns the Manager that while the agent is following technical rules, the customer’s emotional state is leading toward churn, allowing for immediate supervisor intervention.
""")