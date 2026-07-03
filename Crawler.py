# ==========================================================
# Week 2 Assignment - Data Collection Pipeline
#
# Website: http://quotes.toscrape.com
#
# Libraries Used:
#   requests      -> Download webpage
#   BeautifulSoup -> Parse HTML
#   pandas        -> Create and save dataset
# ==========================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd


# ==========================================================
# Function 1: Download a webpage
# ==========================================================
def download_page(url):
    """
    Sends an HTTP GET request to the given URL.
    Returns a BeautifulSoup object if successful.
    Returns None if the request fails.
    """

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Failed to load page ({response.status_code})")
            return None

        # Convert HTML into a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)
        return None


# ==========================================================
# Function 2: Extract all quotes from one page
# ==========================================================
def extract_quotes(soup, page_number, all_quotes, seen_quotes):
    """
    Extracts quote information from one page.

    Parameters:
        soup         -> BeautifulSoup object
        page_number  -> Current page number
        all_quotes   -> List that stores all extracted data
        seen_quotes  -> Set used to avoid duplicate quotes

    Returns:
        True  -> if a next page exists
        False -> if this is the last page
    """

    # Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    # If no quotes are found, stop scraping
    if not quotes:
        print("No quotes found.")
        return False

    print(f"Quotes Found: {len(quotes)}")

    # Loop through every quote
    for quote in quotes:

        # -------------------------------
        # Safe extraction of quote text
        # -------------------------------
        text_tag = quote.find("span", class_="text")

        if text_tag:
            text = text_tag.get_text(strip=True)
        else:
            text = "N/A"

        # -------------------------------
        # Skip duplicate quotes
        # -------------------------------
        if text in seen_quotes:
            continue

        seen_quotes.add(text)

        # -------------------------------
        # Safe extraction of author
        # -------------------------------
        author_tag = quote.find("small", class_="author")

        if author_tag:
            author = author_tag.get_text(strip=True)
        else:
            author = "Unknown"

        # -------------------------------
        # Safe extraction of profile link
        # -------------------------------
        profile_tag = quote.find("a")

        if profile_tag:
            profile = profile_tag.get("href", "")
        else:
            profile = ""

        # -------------------------------
        # Extract tags
        # -------------------------------
        tags = []

        for tag in quote.find_all("a", class_="tag"):
            tags.append(tag.get_text(strip=True))

        # Store quote in dictionary
        quote_data = {
            "Quote": text,
            "Author": author,
            "Profile": profile,
            "Tags": ", ".join(tags),
            "Page": page_number
        }

        # Save dictionary into list
        all_quotes.append(quote_data)

        # Display extracted information
        print("Quote   :", text)
        print("Author  :", author)
        print("Profile :", profile)
        print("Tags    :", ", ".join(tags))
        print("-" * 60)

    # Check whether the Next button exists
    next_button = soup.find("li", class_="next")

    return next_button is not None


# ==========================================================
# Function 3: Save data into CSV
# ==========================================================
def save_to_csv(all_quotes):

    df = pd.DataFrame(all_quotes)

    df.to_csv("quotes.csv", index=False)

    print("\n====================================")
    print("CSV file created successfully!")
    print(f"Total Quotes: {len(df)}")
    print("Saved File : quotes.csv")
    print("====================================")

    print("\nFirst Five Records:\n")
    print(df.head(2))


# ==========================================================
# Function 4: Main Function
# ==========================================================
def main():

    page = 1

    all_quotes = []

    # Set automatically removes duplicates
    seen_quotes = set()

    while True:

        print(f"\nScraping Page {page}...")

        url = f"http://quotes.toscrape.com/page/{page}/"

        # Download webpage
        soup = download_page(url)

        # Stop if page cannot be downloaded
        if soup is None:
            break

        # Extract all quotes
        has_next = extract_quotes(
            soup,
            page,
            all_quotes,
            seen_quotes
        )

        # Stop if there is no next page
        if not has_next:
            print("\nLast page reached.")
            break

        page += 1

    # Save all collected data
    save_to_csv(all_quotes)


# ==========================================================
# Program starts here
# ==========================================================
if __name__ == "__main__":
    main()