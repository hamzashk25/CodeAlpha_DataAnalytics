import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', id='main_table_countries_today')
rows = table.find_all('tr')[8:-8]  # Skip headers & footers

data = []
for row in rows:
    cols = row.find_all('td')
    country = cols[1].text.strip()
    cases = cols[2].text.strip()
    deaths = cols[4].text.strip()
    recovered=cols[6].text.strip()
    active_cases=cols[8].text.strip()
    serious_cases=cols[9].text.strip()
    total_tests=cols[12].text.strip()
    population=cols[14].text.strip()
    data.append([country, cases, deaths,recovered,active_cases,serious_cases,total_tests,population])

df = pd.DataFrame(data, columns=["Country", "Total Cases", "Total Deaths","total Recovered","Active Cases","Serious,Critical","Total Tests","Population"])
print(df.head())
df.to_excel("covid_data.xlsx", index=False)
print("COVID-19 data saved!")