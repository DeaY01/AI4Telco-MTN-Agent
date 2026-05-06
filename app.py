import pandas as pd
import plotly.express as px
import random
import streamlit as st
from ai_core import analyze_complaint  # Unified AI system connection

# --- 1. CORE ENGINE CONFIGURATION ---
st.set_page_config(
    page_title="MTN Retention | Intelligence Hub",
    page_icon="none",
    layout="wide"
)

# --- 2. MTN MODERN DIGITAL IDENTITY (REFINED CSS) ---
st.markdown("""
    <style>
    /* Global Canvas */
    .stApp { background-color: #F4F4F4; color: #000000; font-family: 'Inter', sans-serif; }
    
    /* Branded Header */
    header[data-testid="stHeader"] { 
        background-color: #FFCC00 !important; 
        border-bottom: 2px solid #000000; 
    }

    /* Improved Tab Navigation */
    .stTabs [data-baseweb="tab-list"] { 
        background-color: #FFFFFF; 
        padding: 10px; 
        border-bottom: 1px solid #E0E0E0; 
    }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; 
        font-weight: 700; 
        border: 1px solid #E0E0E0; 
        color: #757575; 
    }
    .stTabs [aria-selected="true"] { 
        background-color: #FFCC00 !important; 
        border: 1px solid #000000 !important; 
        color: #000000 !important; 
    }

    /* Metric Tiles */
    div[data-testid="stMetric"] { 
        background-color: #FFFFFF; 
        border-radius: 0px; 
        padding: 30px !important; 
        border: 1px solid #000000; 
        box-shadow: 6px 6px 0px #000000; 
    }

    /* Intelligence Container */
    .intelligence-container { 
        background: #FFFFFF; 
        border: 1px solid #000000; 
        padding: 40px; 
        box-shadow: 10px 10px 0px #FFCC00; 
    }

    /* MTN Pill Buttons */
    .stButton>button { 
        background: #FFCC00 !important; 
        color: #000000 !important; 
        border: 2px solid #000000 !important; 
        border-radius: 50px !important; 
        font-weight: 900 !important; 
        height: 55px; 
        transition: 0.3s ease;
    }
    .stButton>button:hover { background: #000000 !important; color: #FFCC00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC DATA LAYER ---
def load_retention_data():
    if 'retention_df' not in st.session_state:
        st.session_state.retention_df = pd.DataFrame({
            'customer_index': range(1001, 1051),
            'complains': [random.randint(0, 1) for _ in range(50)],
            'call__failure': [random.randint(0, 50) for _ in range(50)],
            'priority': random.choices(['CRITICAL', 'HIGH', 'MEDIUM'], k=50)
        })
    return st.session_state.retention_df

df = load_retention_data()

# --- 4. BRANDED HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/commons/a/af/MTN_Logo.svg", width=85)
st.markdown("<h1 style='letter-spacing:-2px; font-weight:900; margin-top:-15px;'>RETENTION INTELLIGENCE HUB</h1>", unsafe_allow_html=True)

# --- 5. WORKFLOW SEGMENTATION ---
tab_copilot, tab_trends = st.tabs(["LOYALTY COPILOT", "CHURN ANALYTICS"])

# MODULE 1: LOYALTY COPILOT
with tab_copilot:
    st.markdown("### 01 / INDIVIDUAL RETENTION STRATEGY")
    c1, c2 = st.columns([1, 1.2], gap="large")
    
    with c1:
        st.markdown('<div class="intelligence-container">', unsafe_allow_html=True)
        sub_id = st.selectbox("SEARCH SUBSCRIBER PROFILE", df['customer_index'].unique())
        st.caption("Analyzing real-time usage patterns for churn risk indicators.")
        
        complaint_text = st.text_area("SENTIMENT INPUT", placeholder="Paste specific customer triggers here...", height=100)
        
        if st.button("EXECUTE RETENTION ANALYSIS"):
            metrics = df[df['customer_index'] == sub_id].iloc[0]
            fail_count = metrics['call__failure']
            
            # --- INNOVATION LAYER: Unified AI Call ---
            with st.spinner("Consulting Azure OpenAI Co-pilot..."):
                try:
                    ai_response = analyze_complaint(complaint_text)
                except Exception as e:
                    ai_response = "Error connecting to AI engine. Using local fallback logic."
            
            st.divider()
            
            # Display Intelligence Result
            st.markdown(f"**AI-GENERATED STRATEGY**:")
            st.info(ai_response)
            
            # Operational Risk Flags
            if fail_count > 25:
                st.error("🚩 RISK FLAG: CRITICAL CHURN THREAT")
                st.info("**NEXT BEST ACTION**: Trigger Automated MoMo Refund Protocol.")
            elif 10 <= fail_count <= 25:
                st.warning("⚠️ RISK FLAG: MODERATE ATTRITION RISK")
                st.info("**NEXT BEST ACTION**: Provision 'Appreciation' Data Bonus.")
            else:
                st.success("✅ RISK FLAG: LOYAL / STABLE")
                st.info("**NEXT BEST ACTION**: Log positive sentiment and offer early upgrade path.")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.subheader("Subscriber Failure Profile")
        fig_bar = px.bar(df.head(12), x='customer_index', y='call__failure', 
                         color_discrete_sequence=['#FFCC00'], template="plotly_white")
        fig_bar.update_layout(margin=dict(t=10), plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_bar, use_container_width=True)

# MODULE 2: CHURN ANALYTICS
with tab_trends:
    st.markdown("### 02 / BULK RISK OVERVIEW & DATA INGESTION")
    
    uploaded_file = st.file_uploader("UPLOAD CHURN DATA (CSV)", type="csv")
    if uploaded_file:
        st.session_state.retention_df = pd.read_csv(uploaded_file)
        st.success("Global Retention Data Refreshed.")

    m1, m2, m3 = st.columns(3)
    m1.metric("DISPUTE VOLUME", int(df['complains'].sum()))
    m2.metric("AVG NETWORK FRUSTRATION", f"{df['call__failure'].mean():.1f}")
    m3.metric("RETENTION PRIORITY", "CRITICAL")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    v1, v2 = st.columns(2)
    with v1:
        st.markdown('<div style="background:#FFFFFF; padding:20px; border:1px solid #000000;">', unsafe_allow_html=True)
        st.subheader("Priority Distribution")
        fig_p = px.pie(df, names='priority', color_discrete_sequence=['#000000', '#FFCC00', '#757575'])
        st.plotly_chart(fig_p, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with v2:
        st.markdown('<div style="background:#FFFFFF; padding:20px; border:1px solid #000000;">', unsafe_allow_html=True)
        st.subheader("Historical Churn Trends")
        fig_l = px.line(df, y='call__failure', color_discrete_sequence=['#000000'])
        fig_l.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_l, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)