import streamlit as st
import json
import os

st.title("AI Job Search Agent")

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

        st.success(f"{len(jobs)} jobs loaded")

        for job in jobs:

            st.subheader(job["title"])
            st.write(f"Company: {job['company']}")
            st.write(f"Location: {job['location']}")

            st.markdown(f"[Apply Here]({job['url']})")

            st.divider()
