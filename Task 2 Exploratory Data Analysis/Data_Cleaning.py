import pandas as pd
import numpy as np

# df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
df=pd.read_excel("Covid/covid_data.xlsx")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

# change "N/A" to np.nan it means missing values 
df=df.replace("N/A",np.nan)

df = df.drop(columns=['Serious,Critical'])

# # 1. Drop non-country entities
rows_to_drop = ['Diamond Princess', 'MS Zaandam']
df = df[~df['Country'].isin(rows_to_drop)]

# Fill Active Cases if missing but other two exist
mask_active = df["Active Cases"].isna() & df["Total Deaths"].notna() & df["Total Recovered"].notna()
df.loc[mask_active, "Active Cases"] = df["Total Cases"] - (df["Total Deaths"] + df["Total Recovered"])

# Fill Total Recovered if missing but other two exist
mask_recovered = df["Total Recovered"].isna() & df["Total Deaths"].notna() & df["Active Cases"].notna()
df.loc[mask_recovered, "Total Recovered"] = df["Total Cases"] - (df["Total Deaths"] + df["Active Cases"])

df['Death rate']=df["Total Deaths"] / df["Total Cases"] * 100
df['Recovery rate']=df["Total Recovered"] / df["Total Cases"] * 100
df['Active Cases rate']=df["Active Cases"] / df["Total Cases"] * 100
df['Cases per million']=df["Total Cases"] / df["Population"] * 1e6
df['Death per million']=df["Total Deaths"] / df["Population"] * 1e6
df['Tests per thousand'] = df['Total Tests'] / df['Population'] * 1e3

df.to_excel("Cleaned_Covid_Data_01.xlsx",index=False)