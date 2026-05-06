import pandas as pd
import numpy as np

def clean_all_datasets():
    print("🚀 Starting Data Preprocessing...")

    # --- 1. IRANIAN CHURN (Behavioral Risk) ---
    try:
        risk_df = pd.read_csv("data/Customer Churn.csv")
        # Standardize columns
        risk_df.columns = [c.lower().strip().replace(' ', '_') for c in risk_df.columns]
        # Fill missing with 0 (standard for usage metrics)
        risk_df = risk_df.fillna(0)
        risk_df.to_csv("data/cleaned_risk.csv", index=False)
        print("✅ Risk Dataset: Cleaned (Customer Churn.csv)")
    except Exception as e:
        print(f"❌ Error in Risk Data: {e}")

    # --- 2. KAGGLE TELCO (Customer Segmentation) ---
    try:
        seg_df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
        seg_df.columns = [c.lower().strip().replace(' ', '_') for c in seg_df.columns]
        # 'totalcharges' often has hidden empty strings that need to be numeric
        seg_df['totalcharges'] = pd.to_numeric(seg_df['totalcharges'], errors='coerce').fillna(0)
        seg_df.to_csv("data/cleaned_segmentation.csv", index=False)
        print("✅ Segmentation Dataset: Cleaned (WA_Fn-UseC_-Telco-Customer-Churn.csv)")
    except Exception as e:
        print(f"❌ Error in Segmentation Data: {e}")

    # --- 3. CALL DETAILS (Usage Analysis) ---
    try:
        usage_df = pd.read_csv("data/Call Details-Data.csv")
        usage_df.columns = [c.lower().strip().replace(' ', '_') for c in usage_df.columns]
        # Drop duplicates to keep the data audit-ready
        usage_df = usage_df.drop_duplicates()
        usage_df.to_csv("data/cleaned_usage.csv", index=False)
        print("✅ Usage Dataset: Cleaned (Call Details-Data.csv)")
    except Exception as e:
        print(f"❌ Error in Usage Data: {e}")

    print("\n✨ All datasets are ready for the AI4Teleco-MTN-Agent!")

if __name__ == "__main__":
    clean_all_datasets()