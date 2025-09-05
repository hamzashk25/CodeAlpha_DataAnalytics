import pandas as pd
import numpy as np
import seaborn as sns

# Ask meaningful questions about the dataset before analysis
print("\nQuestions to consider before analysis:")
questions = [
    "Which countries have the highest and lowest death rates?",
    "Which countries have the highest deaths ?",
    "which countries have the highest and lowest recovery rates?",
    "Numerical distribution of cases per million and death per million across countries?",
    "is there any correlation between tests per thousands and cases per million ?"    
]

for q in questions:
    print(q)

# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
df=pd.read_excel("Cleaned_Covid_Data_01.xlsx", sheet_name="Sheet1")

# Explore the data structure, including variables and data types

# Preview the data
print("First 5 rows of the dataset:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Unique countries
print("\nNumber of unique countries:")
print(df['Country'].nunique())

# Summary statistics
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Understand the structure of the data
print("Columns in the dataset:")
print(df.columns)

# Data types and non-null counts
print("\nData Types and Non-Null Counts:")
print(df.shape)

# Data types of each column
print("\nData Types of Each Column:")
print(df.dtypes)

# Check for unique values in each column
print("\nUnique values per column:")
print(df.nunique())


# For the key rate columns, see the average, spread, min, max.
key_metrics = ['Death rate', 'Recovery rate', 'Cases per million', 'Death per million', 'Tests per thousand']
print("\nKey Metrics Summary Statistics:")
print(df[key_metrics].describe())

# Get the median to avoid skew from extreme outliers
print("\nMedian values (less sensitive to outliers):")
print(df[key_metrics].median())


# Top 10 worst affected countries by Deaths per Million
print("\nTOP 10: Deaths per Million")
top_10_death_mil = df.nlargest(10, 'Death per million')[['Country', 'Death per million', 'Total Deaths', 'Population']]
print(top_10_death_mil)

# Top 10 best recovery rates
print("\nTOP 10: Recovery Rate")
top_10_recovery = df.nlargest(10, 'Recovery rate')[['Country', 'Recovery rate', 'Total Cases', 'Total Recovered']]
print(top_10_recovery)

# Bottom 10 testing rates (potential under-reporting)
print("\nBOTTOM 10: Tests per Thousand")
bottom_10_testing = df.nsmallest(10, 'Tests per thousand')[['Country', 'Tests per thousand', 'Total Tests', 'Population']]
print(bottom_10_testing)


