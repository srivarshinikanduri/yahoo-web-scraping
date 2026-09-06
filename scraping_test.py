import requests
from bs4 import BeautifulSoup
import csv
import os

# Yahoo Finance URL
url = "https://finance.yahoo.com/"

# Send request
response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=10
)

print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Page title
print("\nPage Title:")
print(soup.title.get_text(strip=True) if soup.title else "No title")

# Find all links
links = soup.find_all("a")

print("\nTotal Links Found:", len(links))

# Store first 20 links
data = []

for link in links[:20]:

    text = link.get_text(" ", strip=True)
    href = link.get("href")

    if text and href:

        data.append({
            "Link Name": text,
            "URL": href
        })

        print("Text:", text)
        print("URL:", href)
        print("-" * 50)

# Create output folder
os.makedirs("output", exist_ok=True)

# Create CSV
csv_file = "output/yahoo_links.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Link Name", "URL"]
    )

    writer.writeheader()
    writer.writerows(data)

print("\nCSV created successfully!")
print("File location:", csv_file)