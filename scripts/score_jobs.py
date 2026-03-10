import json

# Load scraped jobs
with open("../jobs/scraped_jobs.json") as f:
    jobs = json.load(f)

# Keywords describing your profile
keywords = [
    "product manager",
    "product management",
    "growth",
    "data",
    "ai",
    "analytics",
    "platform",
    "api",
    "technical product",
    "strategy"
]

filtered_jobs = []

for job in jobs:

    title = job["title"].lower()

    score = 0

    for word in keywords:
        if word in title:
            score += 2

    # bonus scoring
    if "senior" in title:
        score += 1

    if "lead" in title:
        score += 1

    job["score"] = score

    if score >= 3:
        filtered_jobs.append(job)

with open("../jobs/filtered_jobs.json","w") as f:
    json.dump(filtered_jobs,f,indent=2)

print("Total jobs:",len(jobs))
print("High match jobs:",len(filtered_jobs))
