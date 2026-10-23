
from pathlib import Path
import pandas as pd

file_path = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

if not file_path.exists():
    raise FileNotFoundError(f"Dataset not found: {file_path}")

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

# Convert TotalCharges to numeric.
# Blank or invalid values become NaN.
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"].astype(str).str.strip(),
    errors="coerce"
)

print("\nMissing values after cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nRows with missing TotalCharges:")
print(
    df.loc[
        df["TotalCharges"].isnull(),
        ["customerID", "tenure", "TotalCharges", "Churn"]
    ]
)

print("\nChurn distribution:")
print(df["Churn"].value_counts())

print("\nChurn percentages:")
print(
    (df["Churn"].value_counts(normalize=True) * 100).round(2)
)

print("\nUpdated data types:")
print(df.dtypes)
