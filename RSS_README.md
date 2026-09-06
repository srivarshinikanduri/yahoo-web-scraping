\# Yahoo RSS Feed Extraction



\## Overview



This module demonstrates \*\*RSS feed-based data extraction from Yahoo Finance using Python\*\*. RSS provides a structured way to collect published content such as article titles, links, publication dates, and summaries without directly parsing the complete Yahoo webpage.



The program reads the available Yahoo Finance RSS feed, parses the RSS/XML content using the `feedparser` library, extracts the required article information, and stores the collected data in a CSV file.



\## Objective



The objective of this method is to understand how RSS feeds can be used for simple and structured data extraction from Yahoo Finance.



\## Technologies Used



\* \*\*Python\*\*

\* \*\*feedparser\*\*

\* \*\*CSV\*\*

\* \*\*Yahoo Finance RSS Feed\*\*



\## RSS Feed URL



The project uses the Yahoo Finance RSS feed for AAPL-related news:



```text

https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL\&region=US\&lang=en-US

```



\## Workflow



```text

Yahoo Finance RSS Feed

&#x20;         ↓

&#x20;     RSS / XML

&#x20;         ↓

&#x20;     feedparser

&#x20;         ↓

&#x20;    Parse Feed

&#x20;         ↓

&#x20;  Extract Article Data

&#x20;         ↓

Title / Link / Published / Summary

&#x20;         ↓

&#x20;      CSV File

```



\## Data Extracted



| Field     | Description               |

| --------- | ------------------------- |

| Title     | Title of the news article |

| Link      | URL of the article        |

| Published | Publication date and time |

| Summary   | Available article summary |



\## How It Works



The Python program first provides the Yahoo Finance RSS feed URL to `feedparser`. The library retrieves and parses the RSS/XML content and makes the feed entries available in Python.



The program then loops through each available article and extracts the title, link, publication date, and summary. The extracted information is stored in a list and finally written to a CSV file.



\## Running the Code



Install the required library:



```bash

pip install feedparser

```



Run the program:



```bash

python rss\_extraction.py

```



The extracted data is saved in:



```text

output/yahoo\_rss.csv

```



\## Example Output



```text

Title

Link

Published

Summary

```



The program also displays the number of articles extracted and the location of the generated CSV file.



\## Advantages



\* Simple to implement

\* Structured RSS/XML data

\* Lightweight compared with webpage scraping

\* Easy to parse using Python

\* Useful for collecting headlines and feed updates

\* Data can easily be stored in CSV format



\## Limitations



\* Only information provided in the RSS feed can be extracted.

\* RSS does not provide all information available on the Yahoo webpage.

\* RSS availability may vary between Yahoo services and pages.

\* Feed structure or availability may change.

\* Yahoo's applicable terms and RSS conditions should be reviewed before using or redistributing feed content.



\## Web Scraping vs RSS



| Feature        | Web Scraping                 | RSS Feed                   |

| -------------- | ---------------------------- | -------------------------- |

| Data Source    | Webpage HTML                 | RSS/XML feed               |

| Structure      | HTML                         | Structured feed            |

| Implementation | More complex                 | Simpler                    |

| Data Available | Depends on webpage           | Limited to feed content    |

| Maintenance    | HTML changes can affect code | Usually simpler            |

| Best For       | Webpage-level data           | Headlines and feed updates |



\## Project Structure



```text

Yahoo webscraping/

│

├── scraping\_test.py

├── rss\_extraction.py

├── README.md

├── RSS\_README.md

└── output/

&#x20;   └── yahoo\_rss.csv

```



\## Project Context



This RSS extraction module is part of a larger \*\*Yahoo Data Extraction project\*\*. The project explores three approaches for collecting Yahoo data:



1\. \*\*Web Scraping\*\* – extracting information from Yahoo webpages.

2\. \*\*RSS Feed\*\* – extracting structured content from available Yahoo RSS feeds.

3\. \*\*API\*\* – accessing data through supported Yahoo APIs.



The three methods are maintained in the same repository for comparison and research purposes.



\## Disclaimer



This project is intended for \*\*educational and research purposes\*\*. Users should review and comply with Yahoo's applicable terms, RSS conditions, policies, and content usage requirements before using extracted data for production, redistribution, or commercial purposes.



\## Author



\*\*Srivarshini\*\*



B.Tech – Computer Science and Engineering



