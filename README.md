# Week 2 - Data Collection Pipelines

## AI Internship - Glaxit Software Company

### Project Overview

This project focuses on collecting data from a website using **Web Scraping**. A Python crawler was developed to scrape quotes from **Quotes to Scrape**, handle multiple pages, extract useful information, and save the collected data into a structured CSV dataset.

---

## Topics Covered

- Web Scraping
- JSON APIs (Introduction)
- Data Ingestion
- Pagination Handling

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

---

## Features

- Scrape data from a website
- Handle multiple pages using pagination
- Extract quote text
- Extract author names
- Extract profile links
- Extract tags
- Handle duplicate posts
- Handle missing text
- Save data into a CSV file

---

## Website Used

```
http://quotes.toscrape.com
```

---

## Project Structure

```
Week2-Data-Collection/
│── Crawler.py
│── quotes.csv
│── requirements.txt
│__ README.md

```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python web_scraper.py
```

---

## Output

The scraped dataset is saved as:

```
quotes.csv
```

Example Output:

| Quote | Author | Profile | Tags | Page |
|------|--------|---------|------|------|
| The world as we have created it... | Albert Einstein | /author/Albert-Einstein | change, deep-thoughts | 1 |

---

## Learning Outcomes

- Understand the basics of web scraping
- Send HTTP requests using Requests
- Parse HTML using BeautifulSoup
- Extract structured data from web pages
- Handle pagination automatically
- Manage duplicate and missing data
- Store scraped data using Pandas
- Export datasets to CSV format

---

## Author

**Hammad Younis Abbasi**

AI Intern – Glaxit Software Company
```
