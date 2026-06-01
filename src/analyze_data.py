import pandas as pd
from pathlib import Path
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference

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


# business-friendly column names for Excel export
revenue_by_membership_export = revenue_by_membership.rename(columns={
    "membership_type": "Membership Type",
    "monthly_fee": "Estimated Monthly Revenue"
})

members_by_referral_export = members_by_referral.rename(columns={
    "referral_source": "Referral Source",
    "member_count": "Member Count"
})

cancellations_by_membership_export = cancellations_by_membership.rename(columns={
    "membership_type": "Membership Type",
    "cancellation_rate": "Cancellation Rate (%)"
})

low_attendance_report_export = low_attendance_report.rename(columns={
    "member_id": "Member ID",
    "membership_type": "Membership Type",
    "monthly_fee": "Monthly Fee",
    "sessions_attended": "Sessions Attended",
    "referral_source": "Referral Source",
    "cancelled": "Cancelled"
})


# Business insights for Excel report
top_membership = revenue_by_membership.iloc[0]
top_referral = members_by_referral.iloc[0]

highest_cancel = cancellations_by_membership.sort_values(
    "cancellation_rate", ascending=False
).iloc[0]

insights = [
    (
        f"The highest revenue membership type is {top_membership['membership_type']} "
        f"with ${top_membership['monthly_fee']:.2f} in estimated monthly revenue."
    ),
    (
        f"The strongest referral source is {top_referral['referral_source']} "
        f"with {top_referral['member_count']} members."
    ),
    (
        f"The membership type with the highest cancellation rate is "
        f"{highest_cancel['membership_type']} at {highest_cancel['cancellation_rate']}%."
    ),
    (
        f"There are {low_attendance_members} members flagged as low-attendance risk."
    )
]

insights_df = pd.DataFrame({
    "Business Insights": insights
})


def add_bar_chart(worksheet, title, data_col, category_col, min_row, max_row, anchor):
    chart = BarChart()
    chart.title = title
    chart.y_axis.title = "Value"
    chart.x_axis.title = ""

    data = Reference(
        worksheet,
        min_col=data_col,
        min_row=min_row,
        max_row=max_row
    )

    categories = Reference(
        worksheet,
        min_col=category_col,
        min_row=min_row + 1,
        max_row=max_row
    )

    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)
    chart.height = 8
    chart.width = 14

    worksheet.add_chart(chart, anchor)


with pd.ExcelWriter("reports/gym_business_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    revenue_by_membership_export.to_excel(writer, sheet_name="Revenue by Membership", index=False)
    members_by_referral_export.to_excel(writer, sheet_name="Referral Sources", index=False)
    cancellations_by_membership_export.to_excel(writer, sheet_name="Cancellation Rates", index=False)
    low_attendance_report_export.to_excel(writer, sheet_name="Low Attendance Risk", index=False)
    insights_df.to_excel(writer, sheet_name="Business Insights", index=False)

    for sheet_name, worksheet in writer.sheets.items():
        for cell in worksheet[1]:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        for column_cells in worksheet.columns:
            max_length = 0
            column_letter = get_column_letter(column_cells[0].column)

            for cell in column_cells:
                if cell.value is not None:
                    max_length = max(max_length, len(str(cell.value)))

            adjusted_width = min(max_length + 3, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width

        worksheet.freeze_panes = "A2"
    



    revenue_sheet = writer.sheets["Revenue by Membership"]
    referral_sheet = writer.sheets["Referral Sources"]
    cancellation_sheet = writer.sheets["Cancellation Rates"]

    add_bar_chart(
        worksheet=revenue_sheet,
        title="Revenue by Membership Type",
        data_col=2,
        category_col=1,
        min_row=1,
        max_row=len(revenue_by_membership_export) + 1,
        anchor="A10"
    )

    add_bar_chart(
        worksheet=referral_sheet,
        title="Members by Referral Source",
        data_col=2,
        category_col=1,
        min_row=1,
        max_row=len(members_by_referral_export) + 1,
        anchor="A10"
    )

    add_bar_chart(
        worksheet=cancellation_sheet,
        title="Cancellation Rate by Membership Type",
        data_col=2,
        category_col=1,
        min_row=1,
        max_row=len(cancellations_by_membership_export) + 1,
        anchor="A10"
    )

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