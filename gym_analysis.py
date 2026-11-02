from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

ops = pd.read_csv(DATA / "august_daily_operations.csv", parse_dates=["date"])
products = pd.read_csv(DATA / "august_product_sales.csv")
renewal_inputs = pd.read_csv(DATA / "renewal_inputs.csv")

# Validation
assert len(ops) == 21
assert ops["date"].is_unique
assert (ops["gross_revenue"] >= 0).all()
assert (ops["member_signins"] > 0).all()
assert products["product"].is_unique

products["retail_revenue"] = products["units_sold"] * products["unit_price"]

# Core KPIs
gross_revenue = ops["gross_revenue"].sum()
member_visits = ops["member_signins"].sum()
avg_weekday_attendance = ops["member_signins"].mean()
avg_weekday_revenue = ops["gross_revenue"].mean()
revenue_per_visit = gross_revenue / member_visits
revenue_attendance_corr = ops["gross_revenue"].corr(ops["member_signins"])

retail_units = int(products["units_sold"].sum())
retail_revenue = products["retail_revenue"].sum()

renewal_map = dict(zip(renewal_inputs["metric"], renewal_inputs["value"]))
member_base = int(renewal_map["approx_active_member_base"])
renewal_rate = float(renewal_map["estimated_renewal_rate"])
membership_price = float(renewal_map["monthly_membership_price"])
estimated_renewals = round(member_base * renewal_rate)
estimated_renewal_revenue = estimated_renewals * membership_price

weekly = (
    ops.groupby("week", sort=False)
       .agg(revenue=("gross_revenue","sum"), visits=("member_signins","sum"))
       .reset_index()
)
weekly["revenue_per_visit"] = weekly["revenue"] / weekly["visits"]

category = (
    products.groupby("category", as_index=False)
            .agg(units=("units_sold","sum"), revenue=("retail_revenue","sum"))
)
category["share_of_retail_revenue"] = category["revenue"] / retail_revenue

summary = pd.DataFrame([
    ["August weekday gross revenue", gross_revenue],
    ["Member visits", member_visits],
    ["Average weekday attendance", avg_weekday_attendance],
    ["Average weekday revenue", avg_weekday_revenue],
    ["Revenue per visit", revenue_per_visit],
    ["Revenue-attendance correlation", revenue_attendance_corr],
    ["Retail units sold", retail_units],
    ["Retail product revenue", retail_revenue],
    ["Estimated renewal rate", renewal_rate],
    ["Estimated monthly renewals", estimated_renewals],
    ["Estimated renewal revenue", estimated_renewal_revenue],
], columns=["metric","value"])

summary.to_csv(OUT / "summary_kpis.csv", index=False)
weekly.to_csv(OUT / "weekly_summary.csv", index=False)
category.to_csv(OUT / "product_category_summary.csv", index=False)

print(summary.to_string(index=False))
