
def load_data(df, output_csv="insights/cleaned_data.csv"):
    print(f"[Load] Saving cleaned data to {output_csv}...")
    df.to_csv(output_csv, index=False)
    print("[Load] Data saved successfully.")
