# AI4Telco-MTN-Agent

**Intelligent Agent Copilot for MTN Customer Service**  
**DSN AI Telco Hackathon 2026**

![MTN](https://img.shields.io/badge/Partner-MTN_Nigeria-blue) 
![Azure_OpenAI](https://img.shields.io/badge/AI-Azure_OpenAI-0078D4)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)

---

### Problem Statement

MTN agents handle thousands of customer complaints daily across voice calls, chat, USSD, and other channels. Due to high volume and lack of intelligent support, agents face slow resolution times, inconsistent decisions, missed churn prevention opportunities, and revenue leakage.

**Targeted Problem Statements**:  
- **Primary**: Customer Analytics (P2)  
- **Secondary**: Risk Management (P1) & Productivity (P4)

---

### Personas

- **Primary Persona**: Customer Retention Manager  
- **Secondary Persona**: Frontline Customer Service Agent

---

### Solution

**AI4Telco-MTN-Agent** is a real-time **AI Copilot** that helps MTN agents:

- Instantly analyze customer complaints
- Recommend the **Next Best Action**
- Generate professional responses to customers
- Flag high-risk cases (Churn & Mass Outage)
- Provide Retention Managers with insights and performance visibility

---

### Key Features

- **Agent Copilot**: Single complaint analysis with Next Best Action
- **Insights Dashboard**: Bulk analysis and trends for supervisors
- Risk flagging and reasoning
- MTN Nigeria contextual intelligence

---

### Tech Stack

- **AI Engine**: Azure OpenAI (`telecom-model` / gpt-4o-mini)
- **Frontend**: Streamlit
- **Core Logic**: Python (`ai_core.py`)
- **Data Processing**: Pandas
- **Deployment**: Streamlit / Render

---


---

## Team Success

| Name                        | Role                          |
|----------------------------|-------------------------------|
| Ajibiye Oladapo Jacob      | Project Lead / AI Engineer    |
| Taiwo Akinmosin            | UI/UX & Presentation          |
| IKO PATRICK OJIYA          | Data Analyst / Backend        |
| Mustapha Lukman Opeyemi    | Documentation & Research      |

---


---

### How to Run Locally

```bash
git clone https://github.com/DeaY01/AI4Telco-MTN-Agent.git
cd AI4Telco-MTN-Agent

# Create virtual environment
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py


Made with ❤️ for MTN Nigeria
AI4Telco Hackathon 2026

