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

         # Additional: Barplot - Purchase Rate by Age Group
        plt.figure(figsize=(8, 5))
        agegroup_rates = df.groupby('AgeGroup')['Purchased'].mean().reset_index()
        sns.barplot(x='AgeGroup', y='Purchased', data=agegroup_rates)
        plt.title('Purchase Rate by Age Group')
        plt.ylabel('Purchase Rate')
        plt.savefig('insights/purchase_rate_by_agegroup.png')
        plt.close()

        # Additional: Heatmap - Correlation of Features
        plt.figure(figsize=(6, 4))
        sns.heatmap(df[['Age', 'EstimatedSalary', 'Purchased']].corr(), annot=True, cmap='coolwarm')
        plt.title('Feature Correlation Heatmap')
        plt.savefig('insights/correlation_heatmap.png')
        plt.close()


        purchase_by_agegroup = df.groupby('AgeGroup')['Purchased'].mean()
        print("\nPurchase Rate by Age Group:")
        print(purchase_by_agegroup)

        

    generate_insights(df_clean)

    print("\n  ETL and insights generation completed successfully.")

if __name__ == "__main__":
    main()
