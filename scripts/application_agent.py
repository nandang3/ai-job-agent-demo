import json

# Load filtered jobs
jobs = json.load(open("../jobs/filtered_jobs.json"))

# Take top 5 jobs
top_jobs = jobs[:5]

resume_summary = """
Senior Product Manager with experience building data platforms,
AI-powered analytics systems, and experimentation frameworks.
Expert in translating customer insights into product strategy,
partnering with engineering and data science teams to launch
scalable products that drive measurable business impact.
"""

output = ""

for job in top_jobs:

    title = job["title"]
    company = job["company"]
    url = job["url"]

    # Resume tailoring
    tailored_resume = f"""
Tailored Resume Summary for {title} at {company}

{resume_summary}

Focus: Emphasize experience with AI platforms, data infrastructure,
and experimentation systems relevant to this role.
"""

    # Referral outreach
    referral_message = f"""
Referral Outreach Message

Hi [Name],

I came across the {title} role at {company} and it aligns closely
with my background building AI and data platform products.

If you’re open to it, I’d appreciate the chance to learn more about
the team and would be grateful for any guidance or referral.

Thanks so much!
"""

    # Interview prep
    interview_prep = f"""
Interview Preparation for {title} at {company}

Likely questions:

1. How would you define product strategy for this role?
2. Describe a data-driven product decision you made.
3. How do you prioritize features in AI-driven products?
4. How do you work with engineering and data science teams?
5. Describe how you measure product success.

Topics to review:

• AI product lifecycle
• Data platform architecture
• Experimentation frameworks
"""

    output += f"""
==================================================
JOB: {title} | {company}
Apply: {url}

{tailored_resume}

{referral_message}

{interview_prep}

==================================================
"""

# Save output
with open("../jobs/daily_application_assistant.txt", "w") as f:
    f.write(output)

print("Application assistant generated for top 5 jobs.")
