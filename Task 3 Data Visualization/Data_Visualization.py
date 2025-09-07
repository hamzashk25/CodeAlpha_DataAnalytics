import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart has a Categorical Comparison
# Pie chart has a Categorical Comparison
# Scatter plot has a Correlation
# Heatmap has a Correlation
# Histogram has a Numerical Distribution
# Box plot has a Distribution
# Line plot has a Trend
# Area plot has a Trend
# Violin plot has a Distribution


df=pd.read_excel("Cleaned_Covid_Data.xlsx",sheet_name="Sheet1")

# print(df.head())

# Pie chart of top 7 countries by total cases
# Pie chart tells us about the share of total cases by top 7 countries
top7 = df.nlargest(7, 'Total Cases')
plt.figure(figsize=(7,7))
plt.pie(top7['Total Cases'], labels=top7['Country'], autopct='%1.1f%%', startangle=140)
plt.title('Top 7 Countries - Share of Global Total Cases')
plt.show()


# Top seven countries that have the highest total deaths 
# Bar Chart of Top 7 countries by total deaths
top7 = df.nlargest(7, "Total Deaths") 
plt.figure(figsize=(10, 6))
plt.bar(top7['Country'], top7["Total Deaths"], color='skyblue')
plt.title("Top 7 Countries by Total Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.show()


# Histogram of death per million
plt.figure(figsize=(10, 5))
plt.hist(df['Death per million'], bins=30, color='salmon', edgecolor='black', alpha=0.7)
plt.axvline(df['Death per million'].median(), color='blue', linestyle='--', label=f'Median: {df["Death per million"].median():.2f}')
plt.title('Distribution of COVID-19 Deaths per Million by Country')
plt.xlabel('Deaths per Million')
plt.ylabel('Number of Countries')
plt.legend()
plt.show()


# Scatter plot of tests per thousand vs cases per million
# Scatter plot tells us about that have more testing have more cases recorded 
plt.figure(figsize=(10, 6))
plt.scatter(df['Tests per thousand'], df['Cases per million'], alpha=0.6)
plt.xscale('log')
plt.yscale('log') 
plt.title('Testing Rate vs. Case Rate')
plt.xlabel('Tests per Thousand (log scale)')
plt.ylabel('Cases per Million (log scale)')
plt.grid(True, which="both", ls="--", linewidth=0.5)
plt.show()


# Heatmap of correlation between numerical columns
# Heatmap tells us where cases are high, deaths are also high.
# its also large population does not guarantee high per million cases or deaths
# its also tells us more testing per population could be linked with higher recovery rate

numerical_df=df.select_dtypes(include=[np.number])
reduced_df=numerical_df.drop(columns=[
    "Active Cases",
    "Total Recovered",
    "Active Cases",
    "Death rate",
])
corr_matrix=reduced_df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Heatmap of COVID-19 Metrics')
plt.tight_layout()
plt.show()