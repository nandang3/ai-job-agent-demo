import streamlit as st
import json
import os
import subprocess

st.title("AI Job Search Agent")
st.caption("AI agents are discovering fresh jobs...")

if st.button("Discover Latest Jobs"):

    with st.spinner("AI agents scanning job sources..."):

        subprocess.run(["python", "scripts/scrape_jobs.py"])
        subprocess.run(["python", "scripts/score_jobs.py"])

    st.success("New jobs discovered!")
query = st.text_input(
    "Ask the AI agent:",
    placeholder="Find me product manager jobs at AI startups"
)

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "jobs", "filtered_jobs.json")

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

        # AI query filter
        if query:

    query_words = query.lower().split()

    filtered_jobs = []

    for job in jobs:

        text = (
            job["title"].lower() +
            job["company"].lower() +
            job["location"].lower()
        )

        if any(word in text for word in query_words):

            filtered_jobs.append(job)

    jobs = filtered_jobs
        st.success(f"{len(jobs)} jobs loaded")

        for job in jobs:

            st.subheader(job["title"])

            st.write(f"Company: {job['company']}")
            st.write(f"Location: {job['location']}")

            # Match score logic
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
