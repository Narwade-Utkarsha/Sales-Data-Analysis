import pandas as pd

# Load dataset using Pandas
df = pd.read_csv("sales_data.csv")

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Dataset Information ---")
df.info()

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Records ---")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["Product"] = df["Product"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n--- After Data Cleaning ---")
print(df.isnull().sum())
print("Duplicate Records:", df.duplicated().sum())
print("Cleaned Shape:", df.shape)

print("\nData Cleaning Completed Successfully!")