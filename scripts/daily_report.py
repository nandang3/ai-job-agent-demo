import json
import os
from datetime import date

os.makedirs("../reports", exist_ok=True)

with open("../jobs/filtered_jobs.json") as f:
    jobs = json.load(f)

report = f"JOB REPORT {date.today()}\n\n"

for job in jobs:

    report += f"""
{job['title']}
{job['company']}
{job['location']}
{job['url']}

"""

with open("../reports/daily_report.txt","w") as f:
    f.write(report)

print("Daily report created.")
