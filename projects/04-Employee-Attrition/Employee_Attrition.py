import pandas as pd
import matplotlib.pyplot as plt

## LOAD DATASET ##

df=pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
print("First 5 Rows:")
print(df.head())

print("\nDataset Informatiom:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

## BASIC ATTRITION ANALYSIS ##

print("\nAttrition Count:")
print(df["Attrition"].value_counts())

attrition_rate =df["Attrition"].value_counts(normalize=True)*100
print("\nAttrition Percentage:")
print(attrition_rate)

## CREATE NEW COLUMNS ##

df["AttritionFlag"] = df["Attrition"].apply(lambda x: 1 if x== 
"Yes" else 0)

bins =[18,25,35,45,55,65]
labels=["18-25","26-35","36-45","46-55","56-65"]

df["AgeGroup"]= pd.cut(df["Age"],bins=bins, labels=labels, include_lowest=True)

## GROUP ANALYSIS ##

print("\nAttrition by Department:")
print(pd.crosstab(df["Department"],df["Attrition"]))

print("\nAttrition by Overtime:")
print(pd.crosstab(df["OverTime"],df["Attrition"]))

print("\nAttrition by Job Role:")
print(pd.crosstab(df["JobRole"],df["Attrition"]))

print("\nAttrition by Group:")
print(pd.crosstab(df["AgeGroup"],df["Attrition"]))

### SAVE CHARTS ###

### CHART 1: Attrition Count ###

plt.figure(figsize=(6,4))
df["Attrition"].value_counts().plot(kind="bar")
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("attrition_count.png")
plt.show()

### CHART 2: Attrition by Department ###

plt.figure(figsize=(8,5))
pd.crosstab(df["Department"],df["Attrition"]).plot(kind="bar")
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("attrition_by_department.png")
plt.show()

### CHART 3: Attrition by Overtime ###

plt.figure(figsize=(6,4))
pd.crosstab(df["OverTime"],df["Attrition"]).plot(kind="bar")
plt.title("Attrition by Overtime")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("attrition_by_overtime.png")
plt.show()

### CHART 4: Attrition by Job Role ###

plt.figure(figsize=(12,6))
pd.crosstab(df["JobRole"],df["Attrition"]).plot(kind="bar")
plt.title("Attrition by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Number of Employees")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("attrition_by_jobrole.png")
plt.show()

### CHART 5: Attrition by Age Group ###

plt.figure(figsize=(8,5))
pd.crosstab(df["AgeGroup"],df["Attrition"]).plot(kind="bar")
plt.title("Attrition by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("attrition_by_agegroup.png")
plt.show()


### EXPORT CLEANED DATA  ###

df.to_csv("cleaned_hr_attrition.csv", index=False)

print("\nCleaned file saved successfully as cleaned_hr_attrition.csv")
print("Charts saved successfully.")