import pandas as pd

def transform_data(df):
    print("[Transform] Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna()

# Optional: adding AgeGroup
    bins = [18, 25, 35, 45, 55, 65]
    labels = ['18-24', '25-34', '35-44', '45-54', '55-64']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    print("[Transform] Data cleaned and age groups added.")
    return df
