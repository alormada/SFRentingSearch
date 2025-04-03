# 🏡 Zillow Automation Bot

This project automates the extraction of real estate listing data from Zillow and submits it to a Google Form for data collection and analysis.

## 📋 Features

- Scrapes property listings (links, addresses, prices) from Zillow.
- Automatically fills and submits a Google Form for each listing using Selenium.
- Designed to be easily extendable for different websites or forms.

## 📁 Project Structure

```
.
├── main.py                  # Entry point for the script
├── ZillowDownload.py       # Handles data extraction from Zillow
├── FormsUpload.py          # Handles data submission to the form
├── .env                    # Stores environment variables
└── README.md               # Project description and usage
```

## 🔐 Environment Variables

Create a `.env` file in the project directory with the following variables:

```
ZILLOW_WEBSITE=https://www.zillow.com/homes/...  # Replace with your Zillow search URL
FORMS_LINK=https://docs.google.com/forms/...     # Replace with your Google Form link
```

## ▶️ How to Run

1. Make sure your `.env` file is configured correctly.
2. Run the main script:

```bash
python main.py
```

This will:
- Scrape listing data from the Zillow search results page.
- Fill out and submit the Google Form for each listing.

## ⚠️ Notes

- The project relies on the structure of Zillow's and Google Form's HTML — changes to those sites may break the script.
- Use this project responsibly and avoid overloading external services with automated requests.
