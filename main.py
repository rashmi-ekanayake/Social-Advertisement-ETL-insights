import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def extract_data(input_path):
    print("[Extract] Reading data...")
    df = pd.read_csv(input_path)
    print(f"[Extract] Loaded {len(df)} rows.")
    return df

def transform_data(df):
    print("[Transform] Cleaning data...")
    df = df.drop_duplicates().dropna()
    # Add age groups
    bins = [17, 24, 34, 44, 54, 64, 100]
    labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
    print("[Transform] Data cleaned and age groups added.")
    return df

def load_data(df, output_path):
    print(f"[Load] Saving cleaned data to {output_path}...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("[Load] Data saved successfully.")

def generate_insights(df):
    print("[Insights] Generating visuals...")

    purchase_rate = df['Purchased'].mean()
    print(f"Overall Purchase Rate: {purchase_rate*100:.2f}%")

    os.makedirs("insights", exist_ok=True)

    # Existing histograms
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='Age', hue='Purchased', multiple='stack', bins=15)
    plt.title('Purchase Distribution by Age')
    plt.savefig('insights/purchase_by_age.png')
    plt.close()

    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='EstimatedSalary', hue='Purchased', multiple='stack', bins=15)
    plt.title('Purchase Distribution by Estimated Salary')
    plt.savefig('insights/purchase_by_salary.png')
    plt.close()

    # Additional barplot: Purchase Rate by Age Group
    plt.figure(figsize=(8, 5))
    agegroup_rates = df.groupby('AgeGroup')['Purchased'].mean().reset_index()
    sns.barplot(x='AgeGroup', y='Purchased', data=agegroup_rates)
    plt.title('Purchase Rate by Age Group')
    plt.ylabel('Purchase Rate')
    plt.savefig('insights/purchase_rate_by_agegroup.png')
    plt.close()

    # Additional heatmap: Feature Correlation
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[['Age', 'EstimatedSalary', 'Purchased']].corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.savefig('insights/correlation_heatmap.png')
    plt.close()

    purchase_by_agegroup = df.groupby('AgeGroup')['Purchased'].mean()
    print("\nPurchase Rate by Age Group:")
    print(purchase_by_agegroup)

class ETLPipeline:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        df = extract_data(self.input_path)
        df_clean = transform_data(df)
        load_data(df_clean, self.output_path)
        generate_insights(df_clean)

def main():
    data_path = "data/social_ads.csv"
    cleaned_path = "insights/cleaned_data.csv"

    pipeline = ETLPipeline(data_path, cleaned_path)
    pipeline.run()

    print("\n✅ ETL and insights generation completed successfully.")

if __name__ == "__main__":
    main()
