import json
import pandas as pd

# Load filtered jobs
with open("../jobs/filtered_jobs.json") as f:
    jobs = json.load(f)

if len(jobs) == 0:
    print("No high match jobs found.")
    exit()

df = pd.DataFrame(jobs)

# Show key fields
columns = ["title","company","location","score","url"]

for col in columns:
    if col not in df.columns:
        df[col] = "N/A"

print("\n===== JOB DASHBOARD =====\n")

print(df[columns].to_string(index=False))

print("\nTotal high match jobs:",len(df))
