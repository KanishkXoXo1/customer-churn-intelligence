
from pathlib import Path
import pandas as pd

RAW_FILE = Path(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)
OUTPUT_FILE = Path(
    "data/processed/customer_churn_cleaned.csv"
)

def main():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {RAW_FILE}")

    df = pd.read_csv(RAW_FILE)

    # Remove accidental whitespace from column names.
    df.columns = df.columns.str.strip()

    # Convert TotalCharges to numeric.
    # Invalid or blank values become NaN.
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"].astype(str).str.strip(),
        errors="coerce"
    )

    missing_before = df["TotalCharges"].isna().sum()
    zero_tenure_missing = (
        df["TotalCharges"].isna() & (df["tenure"] == 0)
    ).sum()

    print("Missing TotalCharges:", missing_before)
    print("Missing charges with zero tenure:", zero_tenure_missing)

    # Apply the documented business assumption:
    # zero-tenure customers have zero accumulated charges.
    eligible = df["TotalCharges"].isna() & (df["tenure"] == 0)
    df.loc[eligible, "TotalCharges"] = 0.0

    # Stop rather than silently invent values for unexpected cases.
    remaining = df["TotalCharges"].isna().sum()
    if remaining:
        raise ValueError(
            f"{remaining} TotalCharges values remain missing. "
            "Investigate them before proceeding."
        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nCleaned dataset saved to:", OUTPUT_FILE)
    print("Final shape:", df.shape)
    print("Remaining missing values:", df.isna().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())

if __name__ == "__main__":
    main()
