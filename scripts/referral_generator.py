import json
import os

os.makedirs("../outreach", exist_ok=True)

with open("../jobs/filtered_jobs.json") as f:
    jobs = json.load(f)

messages = []

for job in jobs:

    msg = f"""
Hi [Name],

I noticed you work at {job['company']}.

I recently applied for the {job['title']} role and would love to learn more about the team and product strategy there.

I have 13+ years of experience in product management, analytics, and cross-functional leadership.

Would you be open to a quick 10-minute chat?

Best,
Nandan
"""

    messages.append(msg)

with open("../outreach/referral_messages.txt","w") as f:
    f.write("\n\n---\n\n".join(messages))

print("Referral messages created.")
