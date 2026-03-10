import streamlit as st
import json
import os

st.title("AI Job Search Agent")
query = st.text_input(
    "Ask the AI agent:",
    placeholder="Find me product manager jobs at AI startups"
)
# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct path to job data
data_path = os.path.join(BASE_DIR, "jobs", "filtered_jobs.json")

# If job file does not exist
if not os.path.exists(data_path):

    st.warning("No jobs available yet.")
    st.write("Run the AI job agent first:")

    st.code("""
cd ~/ai-job-agent/scripts
python scrape_jobs.py
python score_jobs.py
""")

else:

    with open(data_path) as f:
        jobs = json.load(f)

    if len(jobs) == 0:
        st.warning("Job file exists but no jobs were found.")

    else:
if query:

    query_lower = query.lower()

    jobs = [
        j for j in jobs
        if query_lower in j["title"].lower()
        or query_lower in j["company"].lower()
    ]
        st.success(f"{len(jobs)} jobs loaded")

        for job in jobs:

            st.subheader(job["title"])
            st.write(f"Company: {job['company']}")
            st.write(f"Location: {job['location']}")
# Simple AI-style match score
keywords = ["product", "ai", "data", "analytics"]

score = 5

title_lower = job["title"].lower()

for word in keywords:
    if word in title_lower:
        score += 1

score = min(score, 10)

st.write(f"Match Score: {score}/10")
            st.markdown(f"[Apply Here]({job['url']})")

            st.divider()
