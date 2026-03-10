import requests
import json
import feedparser
from bs4 import BeautifulSoup

jobs = []

def relevant_title(title):

    keywords = [
        "product manager",
        "product management",
        "product owner",
        "technical product manager",
        "growth product manager",
        "ai product manager",
        "data product manager",
        "group product manager",
        "product lead"
    ]

    title = title.lower()

    return any(k in title for k in keywords)


def scrape_remoteok():

    print("Scraping RemoteOK...")

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers)
        data = response.json()

        for job in data:

            title = job.get("position")
            company = job.get("company")
            url = job.get("url")

            if not title:
                continue

            if not relevant_title(title):
                continue

            jobs.append({
                "title": title,
                "company": company,
                "location": "Remote",
                "url": url,
                "source": "RemoteOK"
            })

    except Exception as e:
        print("RemoteOK failed:", e)


def scrape_workingnomads():

    print("Scraping WorkingNomads RSS...")

    feed = feedparser.parse(
        "https://www.workingnomads.com/jobsapi/job_feed?category=product"
    )

    for entry in feed.entries:

        title = entry.title
        link = entry.link

        if not relevant_title(title):
            continue

        jobs.append({
            "title": title,
            "company": "Unknown",
            "location": "Remote",
            "url": link,
            "source": "WorkingNomads"
        })


def scrape_yc():

    print("Scraping YC Jobs...")

    url = "https://www.workatastartup.com/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.text, "html.parser")

        for a in soup.find_all("a"):

            title = a.text.strip()

            if not relevant_title(title):
                continue

            link = "https://www.workatastartup.com" + a.get("href", "")

            jobs.append({
                "title": title,
                "company": "YC Startup",
                "location": "Unknown",
                "url": link,
                "source": "YC"
            })

    except Exception as e:
        print("YC scraping failed:", e)


def save_jobs():

    print("Saving jobs...")

    unique = []
    seen = set()

    for job in jobs:

        key = job["title"] + job["company"]

        if key not in seen:
            seen.add(key)
            unique.append(job)

    with open("../jobs/scraped_jobs.json", "w") as f:

        json.dump(unique, f, indent=2)

    print("Total jobs collected:", len(unique))


def main():

    scrape_remoteok()
    scrape_workingnomads()
    scrape_yc()

    save_jobs()


main()
