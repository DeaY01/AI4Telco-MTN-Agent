import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.set_page_config(layout="wide", page_title="MTN Network Intelligence")

# MTN ENTERPRISE BRANDING
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
    .metric-card { background: #F8F9FA; padding: 15px; border-radius: 4px; border-left: 5px solid #FFCC00; }
    .status-label { font-weight: bold; font-size: 0.8rem; color: #666; }
    </style>
    <div class='mtn-header'>
        <h1 style='color:#000; margin:0;'>NETWORK CDR & SIGNAL TRACE</h1>
        <div class='mtn-logo'>MTN</div>
    </div>
""", unsafe_allow_html=True)

st.write("")

# TOP LEVEL KPI BAR: (Slide 01 - Risk Management)
k1, k2, k3, k4 = st.columns(4)
k1.metric("Node Health Index", "94.2%", "-1.4%")
k2.metric("Mean Latency", "42ms", "+4ms")
k3.metric("Packet Loss Trace", "0.08%", "Stable")
k4.metric("Active Churn Risk", "12.4%", "Critical")

st.divider()

col_trace, col_rca = st.columns([2, 1], gap="large")

with col_trace:
    st.subheader("Live Multi-Source Signal Trace")
    st.caption("Aggregating CDR and IPDR metrics in real-time to detect service disruptions.")
    
    # Triple-Threat Metric Selection
    metric_view = st.multiselect(
        "Select Trace Metrics:",
        ["Signal Strength (dBm)", "Data Throughput (Mbps)", "Latency (ms)"],
        default=["Signal Strength (dBm)", "Data Throughput (Mbps)"]
    )
    
    trace_placeholder = st.empty()
    
    # Real-time Simulation Loop
    for i in range(1, 11):
        with trace_placeholder.container():
            t = np.linspace(0, 10, 100)
            
            # Data generation for all metrics to prevent ValueErrors
            signal = np.sin(t + i) * 5 - 85 
            throughput = np.cos(t + i) * 10 + 45
            latency = np.abs(np.sin(t + i) * 12) + 32
            
            df_trace = pd.DataFrame({
                'Time': t, 
                'Signal Strength (dBm)': signal, 
                'Data Throughput (Mbps)': throughput,
                'Latency (ms)': latency
            })
            
            fig = px.line(df_trace, x='Time', y=metric_view,
                          color_discrete_map={
                              'Signal Strength (dBm)': '#000000', 
                              'Data Throughput (Mbps)': '#FFCC00',
                              'Latency (ms)': '#666666'
                          })
            
            fig.update_layout(height=350, margin=dict(l=0, r=0, t=20, b=0), legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig, use_container_width=True)
            time.sleep(0.1)

with col_rca:
    # Automated AI Root Cause Analysis (Slide 03 - Technical Framework)
    st.subheader("Automated AI RCA")
    st.markdown("""
        <div class='metric-card'>
            <span class='status-label'>DETECTED ANOMALY</span><br>
            <strong>Sector Congestion: Lekki-04</strong><br><br>
            <span class='status-label'>ROOT CAUSE</span><br>
            <span>Interference on 1800MHz Band</span><br><br>
            <span class='status-label'>IMPACTED USERS</span><br>
            <strong>1,402 Subscribers</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Predictive Restoration (Success Team Innovation)
    st.subheader("Predictive Restoration")
    st.write("AI Estimated Time to Resolution (ETTR):")
    st.markdown("<h2 style='color:#000; margin:0;'>00:42:15</h2>", unsafe_allow_html=True)
    st.caption("Status: Automated Node Optimization Initiated")
    
    if st.button("Trigger Optimization", use_container_width=True):
        st.success("Optimization Protocol Sent to NOC")

st.divider()

# Regional Risk Heatmap (Slide 02 - Customer Analytics P2)
st.subheader("Regional Risk Heatmap: Lagos Clusters")
# Centered on Lagos Coordinates
map_data = pd.DataFrame(
    np.random.randn(50, 2) / [50, 50] + [6.5244, 3.3792],
    columns=['lat', 'lon']
)
st.map(map_data, color="#FFCC00", size=25)

st.divider()
st.caption("SUCCESS Team Framework | Problem P1: Risk Management | Infrastructure Intelligence Layer")