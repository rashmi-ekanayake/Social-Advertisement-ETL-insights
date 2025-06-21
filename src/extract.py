import pandas as pd

def extract_data(filepath):
    print("[Extract] Reading data...")
    df = pd.read_csv(filepath)
    print(f"[Extract] Loaded {len(df)} rows.")
    return df
