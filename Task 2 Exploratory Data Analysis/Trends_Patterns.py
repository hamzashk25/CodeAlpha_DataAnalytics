import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
df=pd.read_excel("Cleaned_Covid_Data.xlsx", sheet_name="Sheet1")

# Trends 
# Use a log scale because the data is spread over several orders of magnitude
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Total Cases', y='Total Deaths', alpha=0.6)
plt.xscale('log')
plt.yscale('log')
plt.title('Global Trend: Total Cases vs. Total Deaths (Log Scale)')
plt.xlabel('Total Cases (log scale)')
plt.ylabel('Total Deaths (log scale)')
plt.show()
correlation = df['Total Cases'].corr(df['Total Deaths'])
print(f"Correlation coefficient between Total Cases and Total Deaths: {correlation:.3f}")


# Pattern
plt.figure(figsize=(12, 6))
sns.histplot(df['Death rate'], bins=30, kde=True)
plt.axvline(df['Death rate'].median(), color='red', linestyle='--', label=f'Median: {df["Death rate"].median():.2f}%')
plt.title('Distribution of Death Rates (%) by Country')
plt.xlabel('Death Rate (%)')
plt.legend()
plt.show()
print(f"Global Average Death Rate: {df['Death rate'].mean():.2f}%")
print(f"Global Median Death Rate: {df['Death rate'].median():.2f}%")


# Anomaly No 01
# Find countries with a death rate above a extreme threshold, say 4%
# In this anomaly we are looking for countries with very high death rates but not necessarily high case counts
high_death_rate_df = df[df['Death rate'] > 4]
print("Countries with very high Death Rates:")
print(high_death_rate_df[['Country', 'Death rate', 'Total Cases', 'Total Deaths']].sort_values('Death rate', ascending=False))


# Anomaly No 02
# Let's find countries in the top 25% for cases per million but bottom 25% for death rate
# In this anomaly we are looking for countries that have high penetration of the virus but low death rates, which could indicate effective healthcare responses or underreporting of deaths
high_cases = df['Cases per million'].quantile(0.75)
low_death_rate = df['Death rate'].quantile(0.25)
anomaly_df = df[(df['Cases per million'] > high_cases) & (df['Death rate'] < low_death_rate)]
print("\nCountries with high penetration (Cases per Million) but low lethality (Death Rate):")
print(anomaly_df[['Country', 'Death rate', 'Cases per million', 'Total Tests']].sort_values('Death rate'))