# Gym Operations Analysis — August 2026

## Project overview

A local gym tracked daily revenue, member attendance, retail product sales, and membership renewals using handwritten sheets. The purpose of this project was to turn those inconsistent operational records into a structured, traceable analysis that could support business decisions.

The workflow follows a simple analyst process:

**messy records → validation and cleaning → structured data → KPIs → business insights → Excel report**

## Business questions

- How much weekday revenue did the gym generate during August?
- How stable was member traffic across the month?
- Does higher attendance strongly explain higher revenue?
- Which retail products drive unit volume and retail revenue?
- How important are membership renewals to the monthly revenue pattern?

## Data and validation

The source data came from photographed handwritten operational records.

Validation rules used in the project:

- August gross revenue was reconstructed from 21 weekday close logs.
- Week 1 attendance was cross-checked against sign-in sheets.
- Later attendance inputs were confirmed from the gym's established weekday traffic pattern.
- Product names were standardized; 3D and C4 flavor variants were normalized to their parent product.
- Only clearly labeled product entries were counted. Ambiguous or unlabeled tally marks were excluded.
- Day passes and memberships were kept separate from retail product units.
- The approximate 80% renewal rate is an owner-informed near estimate, not an audited cohort measurement.
- Profit margin was not calculated because item-level cost-of-goods data was not sufficiently verified.

## Key performance indicators

| KPI | Result |
|---|---:|
| August weekday gross revenue | **$3,950** |
| Member visits | **801** |
| Average weekday attendance | **38.1** |
| Average weekday revenue | **$188.10** |
| Revenue per visit | **$4.93** |
| Revenue-attendance correlation | **r ≈ 0.30** |
| Retail units sold | **312** |
| Retail product revenue | **$692.50** |
| Estimated renewal rate | **~80%** |
| Estimated monthly renewals | **~40 of ~50 members** |
| Estimated renewal revenue | **~$1,000** |

## Main findings

### 1. Revenue peaks were not explained by traffic alone

Week 1 generated **$1,076** and Week 4 generated **$1,045**, while full-week attendance remained in a relatively narrow **188–197 visit** range. The daily revenue-attendance correlation was only about **0.30**.

**Interpretation:** traffic contributes to revenue, but renewals and transaction mix materially affect daily and weekly revenue.

### 2. Renewal timing aligned with the strongest revenue weeks

The highest-revenue weeks occurred near the beginning and end of the month, when renewal activity was heavier.

This is presented as an **association consistent with renewal timing**, not proof that renewals caused the entire revenue increase.

### 3. Water drove retail volume; pre-workout drove retail dollars

- Water: **147 units**
- 3D + Total War + C4: **148 pre-workout units**
- Pre-workout retail revenue: **$485.50**
- Pre-workout share of retail revenue: **~70%**

**Interpretation:** water is a high-frequency basic purchase, while pre-workout products are the stronger retail revenue category.

### 4. The biggest operational opportunity is better data capture

Handwritten records required manual reconciliation and created ambiguity around tallies, continuation sheets, and renewal status.

A standardized digital sales / attendance / renewal log would make future reporting faster and more reliable.

## Project files

```text
gym_data_report_final/
├── Gym_Data_Report_Interview_Final.xlsx
├── gym_analysis.py
├── README.md
├── VALIDATION_NOTES.md
├── INTERVIEW_TALK_TRACK.md
├── requirements.txt
├── data/
│   ├── august_daily_operations.csv
│   ├── august_product_sales.csv
│   └── renewal_inputs.csv
└── outputs/
    ├── summary_kpis.csv
    ├── weekly_summary.csv
    └── product_category_summary.csv
```

## Tools

- Python
- pandas
- Excel
- GitHub
- Manual source validation

## What this project demonstrates

This project demonstrates the ability to take an unclear real-world operating problem, establish validation rules, organize inconsistent data, calculate useful KPIs, distinguish measured values from estimates, and communicate the resulting business implications.
