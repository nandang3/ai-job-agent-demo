import json
import os

INPUT_FILE = "../jobs/scraped_jobs.json"
OUTPUT_FILE = "../jobs/filtered_jobs.json"

with open(INPUT_FILE) as f:
    jobs = json.load(f)

keywords = [
    "product",
    "product manager",
    "pm",
    "ai",
    "machine learning",
    "data",
    "platform",
]

scored_jobs = []

for job in jobs:

    text = (
        job["title"].lower()
        + job["company"].lower()
        + job["location"].lower()
    )

    score = 0

    for word in keywords:
        if word in text:
            score += 1

    job["score"] = score

    scored_jobs.append(job)

# sort by best match
scored_jobs = sorted(scored_jobs, key=lambda x: x["score"], reverse=True)

# keep top 50 jobs
filtered_jobs = scored_jobs[:50]

os.makedirs("../jobs", exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(filtered_jobs, f, indent=2)

print("Total jobs scraped:", len(jobs))
print("Jobs returned to dashboard:", len(filtered_jobs))
