import pandas as pd
import matplotlib.pyplot as plt

### LOAD DATASET ###

df=pd.read_csv("owid-covid-data.csv")
print(df.head())
print(df.info())
print(df.columns)

### FILTER COUNTRIES ###

countries = ["Canada", "United States", "India", "United Kingdom"]
df2 = df[df["country"].isin(countries)].copy()

### KEEP USEFUL COLUMNS  ###

df2=df2[["date","country","total_cases","new_cases","total_deaths","people_vaccinated"]]

### CONVERT DATE COLUMN  ###

df2["data"] = pd.to_datetime(df2["date"])

### CLEAN MISSING VALUES ###

df2["total_cases"] = df2["total_cases"].fillna(0)
df2["new_cases"] = df2["new_cases"].fillna(0)
df2["total_deaths"] = df2["total_deaths"].fillna(0)
df2["people_vaccinated"] = df2["people_vaccinated"].fillna(0)

### CHECK CLEANED DATA ###

print("Cleaned Data Preview:")
print(df2.head())

print("\nMissing Values:")
print(df2.isnull().sum())

### EXPORT CLEANED DATA FOR TABLEAU ###

df2.to_csv("cleaned_covid_data.csv",index=False)
print("\ncleaned_covid_data.csv exported successfully!")

### GRAPH 1: NEW CASES OVER TIME ###

plt.figure(figsize=(12,6))

for country in countries:
    temp =df2[df2["country"]== country]
    plt.plot(temp["date"], temp["new_cases"], label= country)
    
plt.title("New COVID Cases Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.savefig("covid_cases.png")
plt.show()

### GRAPH 2: TOTAL CASES BY COUNTRY ###

latest = df2.sort_values("date").groupby("country").tail(1)

plt.figure(figsize=(8,5))
plt.bar(latest["country"], latest["total_cases"])

plt.title("Total Cases by Country")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("total_cases.png")
plt.show()

### GRAPH 3: VACCINATION TREND ###

plt.figure(figsize=(12,6))

for country in countries:
    temp= df2[df2["country"] == country]
    plt.plot(temp["date"], temp["people_vaccinated"],label=country)
    
plt.title("People Vaccinated Over Time")
plt.xlabel("Date")
plt.ylabel("People Vaccinated")
plt.legend()
plt.tight_layout()
plt.savefig("vaccination.png")
plt.show()

### GRAPH 4: TOTAL DEATHS BY COUNTRY  ###

plt.figure(figsize=(8,5))
plt.bar(latest["country"], latest["total_deaths"])

plt.title("Total Deaths by Country")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("total_deaths.png")
plt.show()


print("\n All graphs saved successfully!")
