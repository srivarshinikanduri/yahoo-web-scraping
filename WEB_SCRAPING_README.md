# Yahoo Data Extraction – Web Scraping

## Overview

This project demonstrates **web scraping of Yahoo webpages using Python**. The purpose is to collect publicly available webpage information such as page titles, navigation links, link names, and URLs, and store the extracted data for further analysis.

The web scraping method sends an HTTP request to a Yahoo webpage, receives the HTML content, and uses **BeautifulSoup** to parse the webpage. The required HTML elements are identified and their information is extracted programmatically.

## Objective

The main objective of this method is to understand how Yahoo webpage data can be extracted using Python and how the collected information can be organized for further use in data analysis and social media analytics research.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* CSV

## Web Scraping Workflow

```text
Yahoo Webpage
      ↓
HTTP Request using Requests
      ↓
HTML Response
      ↓
BeautifulSoup
      ↓
Find Required HTML Elements
      ↓
Extract Text and URLs
      ↓
Store Data
      ↓
CSV File
```

## Data Extracted

The web scraping code can extract information such as:

| Data       | Description                  |
| ---------- | ---------------------------- |
| Page Title | Title of the Yahoo webpage   |
| Link Name  | Text displayed for each link |
| URL        | Destination URL of the link  |

## Method

The Python program first sends a request to the selected Yahoo webpage using the `Requests` library. After receiving a successful response, the HTML content is passed to `BeautifulSoup`.

BeautifulSoup parses the HTML structure and allows the program to identify elements such as `<a>` tags. The link text and URLs are then extracted and organized into a structured format. The collected information can be saved into a CSV file for further analysis.

## Example

The scraper can identify Yahoo sections such as:

```text
News
Finance
Sports
Weather
Tech
Science
Health
Life
```

along with their corresponding URLs when those links are present in the retrieved webpage.

## Advantages

* Simple and easy to implement
* Useful for extracting webpage-level information
* Does not require an API for basic HTML extraction
* Can collect multiple webpage elements automatically
* Extracted data can be stored in CSV format

## Limitations

* Webpage structures can change over time.
* Dynamically loaded content may not be available through a simple HTTP request.
* Scraping provides only the information available in the retrieved HTML.
* Yahoo's applicable Terms of Service and content usage requirements should be reviewed before using automated collection for production or commercial purposes.

## Project Purpose

This implementation is part of a broader **Yahoo Data Extraction project** that compares three approaches:

1. **Web Scraping** – extracting information from Yahoo webpages.
2. **RSS Feed** – collecting structured feed content from available Yahoo RSS feeds.
3. **API** – accessing data through supported Yahoo APIs.

The three methods are maintained in the same repository for learning, comparison, and research purposes.

## Author

**Srivarshini**

B.Tech – Computer Science and Engineering

## Disclaimer

This project is created for **educational and research purposes**. Users should review and comply with Yahoo's applicable terms, policies, and content usage requirements before using automated data collection or extracted data in production, redistribution, or commercial applications.
