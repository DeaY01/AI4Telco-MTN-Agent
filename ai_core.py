import os

def run_success_logic(complaint_text, arpu=5000):
    """
    Core logic for the SUCCESS Team Solution.
    Implements Business Rule Governance (Slide 06)
    """
    text = complaint_text.lower()
    
    # AI Prediction Layer
    if any(x in text for x in ["data", "mb", "gb", "depletion"]):
        category, base_priority = "Data Services", 0.85
    elif any(x in text for x in ["network", "signal", "tower", "service"]):
        category, base_priority = "Network Infrastructure", 0.90
    elif any(x in text for x in ["charge", "deduct", "bill", "money"]):
        category, base_priority = "Revenue & Billing", 0.75
    else:
        category, base_priority = "General Inquiry", 0.40

    # Rules Engine (Slide 06) - Separation of AI and Action
    sentiment_score = 0.9 if "angry" in text or "port" in text else 0.5
    final_priority = min(1.0, base_priority + (sentiment_score * 0.1))
    
    # NBA Decision (Next Best Action)
    if category == "Data Services":
        nba = "Execute HLR Profile Refresh + Session Audit"
        logic = "Automated: No Financial Compensation (Usage Verified)" if arpu < 15000 else "Grant 250MB Retention Bonus"
    elif category == "Network Infrastructure":
        nba = "Localized Node Congestion Check (Cluster 04)"
        logic = "Escalate to NOC Tier 2 Engineering"
    else:
        nba = "Reconcile Wallet Adjustments"
        logic = "Issue Service Credit to Adjustments Ledger"

    return {
        "category": category,
        "priority": "High" if final_priority > 0.8 else "Medium",
        "nba": nba,
        "logic_applied": logic,
        "risk_flag": "CRITICAL" if final_priority > 0.85 else "STABLE"
    }