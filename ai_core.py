from openai import AzureOpenAI
import json
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "telecom-model")

SYSTEM_PROMPT = """You are an expert MTN Nigeria Senior Customer Service Agent and Team Lead.

Return **only** valid JSON using this exact structure:

{
  "Category": "Network" | "Data" | "Billing" | "SIM" | "Recharge" | "Porting" | "USSD" | "Coverage" | "Voice" | "Other",
  "Sentiment": "Positive" | "Neutral" | "Negative",
  "Priority": "High" | "Medium" | "Low",
  "Suggested_Response": "Short, polite, empathetic reply to customer",
  "Next_Best_Action": "Clear action the agent should take next",
  "Internal_Action": "Credit_Issue" | "Escalate_Technical" | "Refund" | "Follow_Up_Call" | "Account_Review" | "No_Action",
  "Risk_Flag": "High_Churn_Risk" | "Mass_Outage_Possible" | "Low_Risk",
  "Reasoning": "Short explanation"
}

Focus on fast resolution and customer retention."""

def analyze_complaint(complaint: str):
    """Single complaint analysis - for Agent Copilot"""
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Complaint: {complaint}"}
            ],
            temperature=0.3,
            max_tokens=700
        )
        return json.loads(response.choices[0].message.content.strip())
    except Exception as e:
        return {"error": str(e)}

def analyze_bulk_complaints(df: pd.DataFrame, complaint_column: str = "complaint"):
    """Bulk analysis - for Backend/Dashboard"""
    results = []
    for _, row in df.iterrows():
        complaint = str(row[complaint_column])
        result = analyze_complaint(complaint)
        result["original_complaint"] = complaint
        results.append(result)
    
    return pd.DataFrame(results)