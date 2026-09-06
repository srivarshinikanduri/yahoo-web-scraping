# 🟣 Yahoo Data Extraction

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-yellow)
![Feedparser](https://img.shields.io/badge/Feedparser-RSS%2FXML-orange)
![License](https://img.shields.io/badge/License-Educational%20Use-lightgrey)

A project demonstrating **three different approaches** to extracting data from the Yahoo platform: **Web Scraping**, **RSS Feed Extraction**, and **API-based Data Extraction**.

This repository explores how different data-access methods can be used to collect and process Yahoo data in a structured and practical way — comparing each method's advantages, limitations, and best-fit use cases.

---

## 📌 Project Objectives

- Understand different Yahoo data extraction methods
- Extract publicly available webpage information using web scraping
- Collect structured content using Yahoo RSS feeds
- Explore data extraction through supported Yahoo APIs
- Process and organize extracted data for further analysis
- Compare the three approaches based on accessibility, structure, flexibility, and complexity

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python |
| HTTP Requests | Requests |
| HTML Parsing | BeautifulSoup |
| RSS/XML Parsing | Feedparser |
| Data Storage | CSV |
| Data Sources | Yahoo RSS Feeds, Yahoo APIs |
| Version Control | Git & GitHub |

---

## 🔍 Data Extraction Methods

### 1️⃣ Web Scraping

Retrieves the HTML content of a Yahoo webpage using Python's `Requests` library, then uses **BeautifulSoup** to parse the HTML and extract elements such as page titles, link names, and URLs.

```text
Yahoo Webpage
     ↓
Requests
     ↓
HTML Response
     ↓
BeautifulSoup
     ↓
Extract Required Elements
     ↓
Structured Data
     ↓
CSV
```

### 2️⃣ RSS Feed Extraction

Uses a Yahoo Finance RSS feed to collect structured content such as article titles, links, publication dates, and summaries. The `feedparser` library parses the RSS/XML response into a format that can be processed with Python and saved to CSV.

```text
Yahoo RSS Feed
     ↓
RSS / XML
     ↓
Feedparser
     ↓
Parse Feed
     ↓
Extract Article Data
     ↓
CSV
```

### 3️⃣ API-Based Extraction

Explores Yahoo's supported APIs for accessing structured data through official endpoints, using authentication mechanisms such as **OAuth** where required. API availability depends on the specific Yahoo service.

```text
Yahoo API
     ↓
Authentication
     ↓
API Request
     ↓
Structured Response
     ↓
Data Processing
     ↓
CSV / Analysis
```

---

## 📊 Method Comparison

| Method | Data Source | Technology | Main Advantage | Main Limitation |
|---|---|---|---|---|
| **Web Scraping** | Yahoo Webpages | Requests + BeautifulSoup | Flexible webpage extraction | HTML structure can change |
| **RSS Feed** | Yahoo RSS | Feedparser | Simple and structured | Limited to feed content |
| **API** | Supported Yahoo APIs | Python + API requests | Structured and application-friendly | Availability depends on supported APIs |

---

## 📁 Project Structure

```text
yahoo-web-scraping/
│
├── scraping_test.py
├── rss_extraction.py
│
├── WEB_SCRAPING_README.md
├── RSS_README.md
├── README.md
│
└── output/
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/srivarshinikanduri/yahoo-web-scraping.git
```

**2. Navigate to the project**
```bash
cd yahoo-web-scraping
```

**3. Install the required Python libraries**
```bash
pip install requests beautifulsoup4 feedparser
```

**4. Run the web scraping code**
```bash
python scraping_test.py
```

**5. Run the RSS extraction code**
```bash
python rss_extraction.py
```

---

## 💡 Key Findings

There is **no single extraction method that is best for every Yahoo service**:

- **Web scraping** is useful when information is available directly in webpage HTML.
- **RSS feeds** are useful when structured feed content is available.
- **APIs** are the preferred approach when an appropriate official API endpoint is available.

The right extraction method ultimately depends on the specific Yahoo service being investigated and the data it exposes.

---

## 🌐 Applications

- Data collection
- Web data analysis
- News and content monitoring
- Social media analytics research
- Market and financial information research
- Learning API, RSS, and web scraping techniques

---

## ⚠️ Important Note

This project is developed for **educational and research purposes**. Before performing automated data collection or using extracted data in production, redistribution, or commercial applications, users should review and comply with Yahoo's applicable terms, policies, API requirements, RSS conditions, and content usage restrictions.

---

## 👩‍💻 Author

**Srivarshini Kanduri**
B.Tech – Computer Science and Engineering
