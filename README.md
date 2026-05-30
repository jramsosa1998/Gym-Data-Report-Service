# Gym Revenue & Member Churn Business Report

## Project Overview

This project analyzes messy gym membership data and turns it into a cleaned business report. I built it to show how Python, pandas, and Excel can be used to clean raw business data, calculate useful metrics, and create a report that supports real-world decision-making.

The project uses simulated gym data that is designed to resemble the type of messy spreadsheet data a small gym or fitness business may deal with. The final output is a structured Excel report that management could use to better understand revenue, membership performance, cancellation patterns, referral sources, and low-attendance risk members.


## Business Problem

Small gyms often track members, payments, attendance, referrals, and cancellations in spreadsheets. Over time, these spreadsheets can become messy due to duplicate rows, inconsistent formatting, missing values, and unclear category labels.

This project solves that problem by cleaning the raw data, creating useful business metrics, and exporting a structured Excel report that can support better business decisions.


## Why I Built This

From my experience working in a gym environment, I learned that spreadsheets can become messy quickly when tracking members, payments, attendance, referrals, and cancellations. Messy data slows down decision-making and makes it harder for management to understand what is happening in the business.

I wanted to combine that real-world gym experience with the analytical mindset I developed through my physics background. Physics trained me to think in terms of systems, patterns, assumptions, and measurable outcomes. In this project, I applied that same mindset to a practical business problem: turning raw membership data into a clean, organized, and management-ready report.

I also understand the gym environment through years of training and observing how member behavior changes over time. Signups, attendance, training goals, and retention can shift depending on the season, the type of gym, and the culture of the facility. This made the project a practical way to connect data analysis with a business setting I understand.


## Tools Used

* Python
* pandas
* Excel
* CSV
* Data cleaning
* Business reporting

## Dataset Description

The dataset contains simulated gym membership records with fields such as:

* Member ID
* Signup date
* Membership type
* Monthly fee
* Sessions attended
* Personal training package status
* Cancellation status
* Age group
* Referral source

The raw dataset intentionally includes messy data issues such as duplicate records, inconsistent cancellation labels, missing values, and monthly fees stored as both text and numbers.

## Business Questions

This project answers the following questions:

1. How many total members are in the dataset?
2. How many members are currently active?
3. What is the estimated monthly revenue from active members?
4. Which membership type generates the most revenue?
5. Which referral source brings in the most members?
6. Which membership types have the highest cancellation rates?
7. Which members may be at risk due to low attendance?

## My Role

For this project, I designed the full workflow from raw data to final report. I created the simulated dataset, cleaned the messy data using Python and pandas, calculated business metrics, and exported the results into a multi-sheet Excel report.

The goal was to turn raw spreadsheet-style data into something professional, reproducible, and useful for decision-making. This workflow could be adapted for small businesses that need to clean messy Excel or CSV files and turn them into clear reports.

## Project Workflow

### 1. Generate Messy Data

The script `generate_demo_data.py` creates a simulated gym membership dataset with realistic messy data problems.

### 2. Clean the Data

The script `clean_data.py` performs the main cleaning steps:

* Standardizes column names
* Removes duplicate rows
* Converts signup dates into datetime format
* Cleans monthly fee values
* Converts monthly fees into numeric values
* Standardizes cancellation status values
* Fills missing cancellation values
* Creates a boolean cancellation column
* Standardizes personal training package values
* Creates a signup month column
* Flags low-attendance risk members

### 3. Analyze the Data

The script `analyze_data.py` calculates key business metrics and creates report tables:

* Summary metrics
* Revenue by membership type
* Member count by referral source
* Cancellation rate by membership type
* Low-attendance risk member list

### 4. Export Business Report

The final output is a multi-sheet Excel report:

```text
reports/gym_business_report.xlsx
```

The Excel report includes:

* Summary
* Revenue by Membership
* Referral Sources
* Cancellation Rates
* Low Attendance Risk

## Files in This Project

```text
gym-data-report-service/
│
├── data/
│   ├── raw/
│   │   └── gym_members_dirty.csv
│   └── cleaned/
│       └── gym_members_cleaned.csv
│
├── reports/
│   └── gym_business_report.xlsx
│
├── src/
│   ├── generate_demo_data.py
│   ├── clean_data.py
│   └── analyze_data.py
│
└── README.md
```

## How to Run This Project

Run the scripts in this order:

```bash
python src/generate_demo_data.py
python src/clean_data.py
python src/analyze_data.py
```

After running the scripts, the cleaned dataset will be saved here:

```text
data/cleaned/gym_members_cleaned.csv
```

The final Excel report will be saved here:

```text
reports/gym_business_report.xlsx
```

## Key Metrics Created

The report includes:

* Total members
* Active members
* Cancelled members
* Estimated monthly revenue
* Average sessions attended
* Low-attendance risk members
* Revenue by membership type
* Referral source performance
* Cancellation rate by membership type

## Skills Demonstrated

This project demonstrates:

* Cleaning messy CSV data
* Handling missing values
* Removing duplicate rows
* Standardizing inconsistent text values
* Converting string values into numeric values
* Creating business metrics
* Grouping and aggregating data with pandas
* Exporting multi-sheet Excel reports
* Translating raw data into business insights
* Building a repeatable reporting workflow
* Applying analytical problem-solving from a physics background to a business data model

## Business Value

This workflow can help a small business owner quickly understand:

* How much revenue the business is generating
* Which membership types are most valuable
* Which marketing channels bring in the most members
* Where cancellations are happening
* Which members may need retention outreach

Instead of manually reviewing messy spreadsheets, the business receives a cleaned dataset and a clear Excel report.

## Next Improvements

Future improvements could include:

* Adding charts to the Excel report
* Creating a dashboard-style summary page
* Adding SQL analysis using the cleaned dataset
* Building a reusable reporting template for other small businesses
* Creating a Streamlit dashboard version
* Adding customer lifetime value estimates
* Adding monthly trend analysis
