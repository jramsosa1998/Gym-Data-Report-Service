import pandas as pd
from pathlib import Path

Path("reports").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/cleaned/gym_members_cleaned.csv")

# Core business metrics
total_members = len(df)
active_members = len(df[df["cancelled"] == False])
cancelled_members = len(df[df["cancelled"] == True])
monthly_revenue = df[df["cancelled"] == False]["monthly_fee"].sum()
average_attendance = df["sessions_attended"].mean()
low_attendance_members = df["low_attendance_risk"].sum()

summary = pd.DataFrame({
    "Metric": [
        "Total Members",
        "Active Members",
        "Cancelled Members",
        "Estimated Monthly Revenue",
        "Average Sessions Attended",
        "Low Attendance Risk Members"
    ],
    "Value": [
        total_members,
        active_members,
        cancelled_members,
        round(monthly_revenue, 2),
        round(average_attendance, 2),
        low_attendance_members
    ]
})

revenue_by_membership = (
    df[df["cancelled"] == False]
    .groupby("membership_type")["monthly_fee"]
    .sum()
    .reset_index()
    .sort_values("monthly_fee", ascending=False)
)

members_by_referral = (
    df.groupby("referral_source")["member_id"]
    .count()
    .reset_index()
    .rename(columns={"member_id": "member_count"})
    .sort_values("member_count", ascending=False)
)

cancellations_by_membership = (
    df.groupby("membership_type")["cancelled"]
    .mean()
    .reset_index()
    .rename(columns={"cancelled": "cancellation_rate"})
)

cancellations_by_membership["cancellation_rate"] = (
    cancellations_by_membership["cancellation_rate"] * 100
).round(2)

low_attendance_report = df[df["low_attendance_risk"] == True][[
    "member_id",
    "membership_type",
    "monthly_fee",
    "sessions_attended",
    "referral_source",
    "cancelled"
]]

with pd.ExcelWriter("reports/gym_business_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    revenue_by_membership.to_excel(writer, sheet_name="Revenue by Membership", index=False)
    members_by_referral.to_excel(writer, sheet_name="Referral Sources", index=False)
    cancellations_by_membership.to_excel(writer, sheet_name="Cancellation Rates", index=False)
    low_attendance_report.to_excel(writer, sheet_name="Low Attendance Risk", index=False)

print("Business report created: reports/gym_business_report.xlsx")
print(summary)





print("\n--- Business Insights ---")

top_membership = revenue_by_membership.iloc[0]

top_referral = members_by_referral.iloc[0]

highest_cancel = cancellations_by_membership.sort_values(
    "cancellation_rate", ascending=False
).iloc[0]

print(
    f"The highest revenue membership type is {top_membership['membership_type']} "
    f"with ${top_membership['monthly_fee']:.2f} in estimated monthly revenue."
)

print(
    f"The strongest referral source is {top_referral['referral_source']} "
    f"with {top_referral['member_count']} members."
)

print(
    f"The membership type with the highest cancellation rate is "
    f"{highest_cancel['membership_type']} at {highest_cancel['cancellation_rate']}%."
)

print(
    f"There are {low_attendance_members} members flagged as low-attendance risk."
)