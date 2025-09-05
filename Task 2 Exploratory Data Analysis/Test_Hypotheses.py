import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Test hypotheses and validate assumptions using statistics and visualization
df=pd.read_excel("Cleaned_Covid_Data_01.xlsx", sheet_name="Sheet1")

# Hypothesis: Higher testing rates correlate with lower death rates
plt.figure(figsize=(8,6))
sns.scatterplot(x='Tests per thousand', y='Death rate', data=df)
plt.title('Testing Rate vs Death Rate')
plt.xlabel('Tests per Thousand')
plt.ylabel('Death Rate (%)')
plt.show()

# Hypothesis: Recovery rate distribution
plt.figure(figsize=(8,6))
sns.histplot(df['Recovery rate'], bins=20, kde=True)
plt.title('Distribution of Recovery Rate')
plt.xlabel('Recovery Rate (%)')
plt.ylabel('Frequency')
plt.show()


# Detect potential data issues or problems to address in further analysis
# It is important to check for negative values in columns where they should not exist
key_metrics = ['Death rate', 'Recovery rate', 'Cases per million', 'Death per million', 'Tests per thousand']
print("\nChecking for negative values in key metrics (should not occur):")
for col in key_metrics:
    negatives = df[df[col] < 0]
    if not negatives.empty:
        print(f"Negative values found in {col}:")
        print(negatives[['Country', col]])
    else:
        print(f"No negative values in {col}.")

print("\nChecking for missing values in key metrics:")
print(df[key_metrics].isnull().sum())