import pandas as pd

filename = input("Enter file name (.csv/.xls/.xlsx): ").strip()

if filename.lower().endswith(".csv"):
    df = pd.read_csv(filename)
elif filename.lower().endswith(".xls") or filename.lower().endswith(".xlsx"):
    df = pd.read_excel(filename)
else:
    print("Invalid file format. Please provide a .csv, .xls, or .xlsx file.")
    raise SystemExit

print("\nOriginal dataframe:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

# Fill numeric missing values
for col in df.select_dtypes(include="number").columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mean())

# Fill categorical missing values
for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any():
        mode_value = df[col].mode(dropna=True)
        if not mode_value.empty:
            df[col] = df[col].fillna(mode_value.iloc[0])
        else:
            df[col] = df[col].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

print("\nPreprocessed dataframe:")
print(df)

df.to_csv("preprocessed_data.csv", index=False)
print("\nPreprocessed data saved to 'preprocessed_data.csv'.")