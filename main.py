from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from pathlib import Path

def main():
    data_path = Path("data/social_ads.csv")
    cleaned_path = Path("insights/cleaned_data.csv")

    df = extract_data(data_path)
    df_clean = transform_data(df)
    load_data(df_clean, cleaned_path)

    # Import generate_insights here to avoid circular imports
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os

    def generate_insights(df):
        print("[Insights] Generating visuals...")

        purchase_rate = df['Purchased'].mean()
        print(f"Overall Purchase Rate: {purchase_rate*100:.2f}%")

        os.makedirs("insights", exist_ok=True)

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

        purchase_by_agegroup = df.groupby('AgeGroup')['Purchased'].mean()
        print("\nPurchase Rate by Age Group:")
        print(purchase_by_agegroup)

    generate_insights(df_clean)

    print("\n  ETL and insights generation completed successfully.")

if __name__ == "__main__":
    main()
