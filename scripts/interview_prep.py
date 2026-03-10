import json
import os

os.makedirs("../interview_prep", exist_ok=True)

with open("../jobs/filtered_jobs.json") as f:
    jobs = json.load(f)

questions = []

for job in jobs:

    q = f"""
INTERVIEW PREP
Company: {job['company']}
Role: {job['title']}

Possible questions:

1. How would you define success for this product?
2. How would you prioritize features in this roadmap?
3. Describe a time you used data to influence a product decision.
4. How would you improve user retention?
5. How do you collaborate with engineering and design teams?
"""

    questions.append(q)

with open("../interview_prep/interview_questions.txt","w") as f:
    f.write("\n\n".join(questions))

print("Interview prep generated.")
