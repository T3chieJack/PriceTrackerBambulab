# 🧾 Bambu Lab Filament Price Tracker

![Scrape Status](https://github.com/T3chieJack/PriceTrackerBambulab/actions/workflows/scrape.yml/badge.svg)

This project automatically tracks and logs the latest filament prices from the [Bambu Lab EU Store](https://eu.store.bambulab.com/collections/filament). It uses a headless browser to scrape dynamically loaded prices, and updates them to this repository every 6 hours via GitHub Actions.

---

## 🚀 Features

- 🔍 Scrapes all available Bambu Lab filament prices from the EU store
- 🧠 Handles JavaScript-loaded content using [Playwright](https://playwright.dev/)
- 🕒 Runs automatically every 6 hours using GitHub Actions
- 💾 Saves price data to `prices.json` in this repository
- 📡 Can be extended to power dashboards, alerts, and price history trackers

---

## 📂 Output Example (`prices.json`)


[
  {
    "title": "PLA Basic - Cool Gray",
    "price": "€21,99"
  },
  {
    "title": "PLA Basic - Red",
    "price": "€21,99"
  }
]
## ⚙️ How It Works
scraper.py uses Playwright to simulate a browser and extract filament prices.

GitHub Actions (in .github/workflows/scrape.yml) runs the scraper every 6 hours.

prices.json is committed and pushed if prices have changed.

🛠️ Tech Stack
Python 3.11

Playwright (headless browser control)

GitHub Actions (CI/CD automation)

## 💻 Local Setup

🧩 Setup for Local Use
bash
Copy
Edit
git clone https://github.com/T3chieJack/PriceTrackerBambulab.git
cd PriceTrackerBambulab
pip install -r requirements.txt
python -m playwright install
python scraper.py
This will generate a fresh prices.json with the latest scraped data.
## 🗒️ Noticeboard
📬 Future Plans
📈 Track historical price changes

📊 Generate CSV or chart-based outputs

🌐 GitHub Pages dashboard

📣 Alert system for price drops (e.g., Discord/Telegram bot)

🤖 Maintained by @T3chieJack
