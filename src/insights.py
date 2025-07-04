import os
import seaborn as sns
import matplotlib.pyplot as plt

def generate_insights(df):
    print("[Insights] Generating visuals...")

    # Overall purchase rate
    purchase_rate = df['Purchased'].mean()
    print(f"Overall Purchase Rate: {purchase_rate*100:.2f}%")

    os.makedirs("insights", exist_ok=True)

    # Purchase distribution by Age
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='Age', hue='Purchased', multiple='stack', bins=15)
    plt.title('Purchase Distribution by Age')
    plt.savefig('insights/purchase_by_age.png')
    plt.close()

    # Purchase distribution by Estimated Salary
    plt.figure(figsize=(8,5))
    sns.histplot(data=df, x='EstimatedSalary', hue='Purchased', multiple='stack', bins=15)
    plt.title('Purchase Distribution by Estimated Salary')
    plt.savefig('insights/purchase_by_salary.png')
    plt.close()

    # Purchase rate by AgeGroup
    purchase_by_agegroup = df.groupby('AgeGroup')['Purchased'].mean()
    print("\nPurchase Rate by Age Group:")
    print(purchase_by_agegroup)
