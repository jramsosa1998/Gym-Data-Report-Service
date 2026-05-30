import pandas as pd
from pathlib import Path

Path("data/cleaned").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/raw/gym_members_dirty.csv")

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove duplicates
df = df.drop_duplicates()

# Convert signup date
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

# Clean monthly fee
df["monthly_fee"] = (
    df["monthly_fee"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.strip()
)

df["monthly_fee"] = pd.to_numeric(df["monthly_fee"], errors="coerce")

# Clean cancellation status
df["cancellation_status"] = (
    df["cancellation_status"]
    .fillna("No")
    .astype(str)
    .str.strip()
    .str.lower()
)

df["cancelled"] = df["cancellation_status"].map({
    "yes": True,
    "no": False,
    "": False
})

df["cancelled"] = df["cancelled"].fillna(False)

# Clean personal training package
df["personal_training_package"] = (
    df["personal_training_package"]
    .fillna("No")
    .astype(str)
    .str.strip()
    .str.title()
)

df["personal_training_package"] = df["personal_training_package"].replace("", "No")

# Add useful columns
df["signup_month"] = df["signup_date"].dt.to_period("M").astype(str)

df["low_attendance_risk"] = df["sessions_attended"] < 4

df.to_csv("data/cleaned/gym_members_cleaned.csv", index=False)

print("Cleaned dataset saved.")
print(df.head())