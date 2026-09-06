import feedparser
import csv
import os

url = "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US"

print("Reading Yahoo RSS feed...")

feed = feedparser.parse(url)

print("Feed title:", feed.feed.get("title", "No title"))
print("Number of articles:", len(feed.entries))

articles = []

for item in feed.entries:

    articles.append({
        "title": item.get("title", ""),
        "link": item.get("link", ""),
        "published": item.get("published", ""),
        "summary": item.get("summary", "")
    })

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

with open(
    "output/yahoo_rss.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "link", "published", "summary"]
    )

    writer.writeheader()
    writer.writerows(articles)

print(f"Saved {len(articles)} articles.")
print("CSV location: output/yahoo_rss.csv")