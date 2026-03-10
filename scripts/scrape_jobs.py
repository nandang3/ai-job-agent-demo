import requests
import json
import os
import feedparser

jobs = []

def add_job(title, company, location, url):
    jobs.append({
        "title": title,
        "company": company,
        "location": location,
        "url": url
    })


def scrape_remoteok():

    print("Scraping RemoteOK...")

    url = "https://remoteok.com/api"

    data = requests.get(url).json()

    for job in data[1:50]:

        add_job(
            job.get("position",""),
            job.get("company",""),
            "Remote",
            job.get("url","")
        )


def scrape_workingnomads():

    print("Scraping WorkingNomads RSS...")

    feed = feedparser.parse(
        "https://www.workingnomads.com/jobsapi/job_feed"
    )

    for entry in feed.entries[:50]:

        add_job(
            entry.title,
            "Unknown",
            "Remote",
            entry.link
        )
def scrape_ai_jobs():

    print("Scraping AI Jobs RSS...")

    feed = feedparser.parse(
        "https://aijobs.com/feed/"
    )

    for entry in feed.entries[:50]:

        add_job(
            entry.title,
            "AI Company",
            "Remote",
            entry.link
        )

def scrape_weworkremotely():

    print("Scraping WeWorkRemotely RSS...")

    feed = feedparser.parse(
        "https://weworkremotely.com/remote-jobs.rss"
    )

    for entry in feed.entries[:50]:

        add_job(
            entry.title,
            "Unknown",
            "Remote",
            entry.link
        )


def save_jobs():

    print("Saving jobs...")

    os.makedirs("../jobs", exist_ok=True)

    with open("../jobs/scraped_jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)


def main():

    scrape_remoteok()
    scrape_workingnomads()
    scrape_weworkremotely()
    scrape_ai_jobs()
    save_jobs()


if __name__ == "__main__":
    main()
