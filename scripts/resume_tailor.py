import json
import os

os.makedirs("../resumes", exist_ok=True)

with open("../jobs/filtered_jobs.json") as f:
    jobs = json.load(f)

with open("../resumes/base_resume.txt") as f:
    base = f.read()

for job in jobs:

    title = job["title"]
    company = job["company"]

    tailored = f"""
{base}

TARGET ROLE
{title} at {company}

RELEVANT STRENGTHS
• Product strategy & roadmap leadership
• Data-driven decision making
• SQL and analytics expertise
• Cross-functional leadership
• Growth and retention optimization
"""

    filename = f"../resumes/resume_{company}.txt".replace(" ","_")

    with open(filename,"w") as f:
        f.write(tailored)

    print("created:",filename)
