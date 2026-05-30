import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

random.seed(42)

Path("data/raw").mkdir(parents=True, exist_ok=True)

membership_types = ["Basic", "Premium", "Student", "Family"]
referral_sources = ["Instagram", "Google", "Walk-in", "Friend", "Facebook"]
cancel_statuses = ["Yes", "No", "no", "YES", "", None]

rows = []

for i in range(1, 301):
    signup_date = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 330))

    membership = random.choice(membership_types)

    if membership == "Basic":
        fee = random.choice(["$29.99", "29.99", 29.99])
    elif membership == "Premium":
        fee = random.choice(["$59.99", "59.99", 59.99])
    elif membership == "Student":
        fee = random.choice(["$24.99", "24.99", 24.99])
    else:
        fee = random.choice(["$89.99", "89.99", 89.99])

    rows.append({
        "Member ID": i,
        "Signup Date": signup_date.strftime("%m/%d/%Y"),
        "Membership Type": membership,
        "Monthly Fee": fee,
        "Sessions Attended": random.randint(0, 30),
        "Personal Training Package": random.choice(["Yes", "No", ""]),
        "Cancellation Status": random.choice(cancel_statuses),
        "Age Group": random.choice(["18-24", "25-34", "35-44", "45-54", "55+"]),
        "Referral Source": random.choice(referral_sources)
    })

df = pd.DataFrame(rows)


df = pd.concat([df, df.sample(10, random_state=42)], ignore_index=True)

df.to_csv("data/raw/gym_members_dirty.csv", index=False)

print("Dirty gym dataset created.")