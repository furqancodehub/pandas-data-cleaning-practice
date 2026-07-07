import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("sales_dataset.csv")

# Inspection
print(df.head())
df.info()
print(df.shape)
print(df.columns)

# Finding Problems

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)

# Actual Cleaning

df["Sales"] = pd.to_numeric(df["Sales"] , errors="coerce")
df["Sales"] = df["Sales"].fillna(0)
df = df.drop_duplicates()
print(df[df.duplicated()])
print(df.duplicated().sum())
sns.barplot(data=df, x="Category", y="Sales")
plt.show()
sns.countplot(data=df, x="City")
plt.show()
sns.histplot(data=df, x="Sales")
plt.show()
sns.lineplot(data=df, x="OrderDate", y="Sales")
plt.show()

df.to_csv("sales_dataset_cleaned.csv",index=False)
