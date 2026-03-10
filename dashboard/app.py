import streamlit as st
import json
import os

st.title("AI Job Search Agent")

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct path
data_path = os.path.join(BASE_DIR, "jobs", "filtered_jobs.json")

if not os.path.exists(data_path):

    st.error("Job data not found.")
    st.write("Run these commands first:")

    st.code("""
cd ~/ai-job-agent/scripts
python scrape_jobs.py
python score_jobs.py
""")

else:

    jobs = json.load(open(data_path))

    st.success(f"{len(jobs)} jobs loaded")

    for job in jobs:

        st.subheader(job["title"])
        st.write(job["company"])
        st.write(job["location"])

        st.markdown(f"[Apply Here]({job['url']})")
