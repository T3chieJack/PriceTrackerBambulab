# 🧾 Bambu Lab Filament Price Tracker

![Scrape Status](https://github.com/T3chieJack/PriceTrackerBambulab/actions/workflows/scrape.yml/badge.svg)

This project automatically tracks and logs the latest filament prices from the [Bambu Lab EU Store](https://eu.store.bambulab.com/collections/filament). It uses a headless browser to scrape dynamically loaded prices, and updates them to this repository every 6 hours via GitHub Actions.

## 🚀 Features

- 🔍 Scrapes all available Bambu Lab filament prices from the EU store
- 🧠 Handles JavaScript-loaded content using [Playwright](https://playwright.dev/)
- 🕒 Runs automatically every 6 hours using GitHub Actions
- 💾 Saves price data to `prices.json` in this repository
- 📡 Can be extended to power dashboards, alerts, and price history trackers

## 📂 Output Example (`prices.json`)

```json
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
```json
⚙️ How It Works
scraper.py uses Playwright to simulate a browser and extract filament prices.

GitHub Actions (in .github/workflows/scrape.yml) runs the scraper every 6 hours.

prices.json is committed and pushed if prices change.

🛠️ Tech Stack
Python 3.11

Playwright for headless browser control

GitHub Actions for automation

🧩 Setup for Local Use
bash
Copy
Edit
git clone https://github.com/T3chieJack/PriceTrackerBambulab.git
cd PriceTrackerBambulab
pip install -r requirements.txt
python -m playwright install
python scraper.py
This will output prices.json with the current prices.

📬 Future Plans
Track historical price changes

Generate CSV or chart-based outputs

GitHub Pages dashboard

Alert system for price drops

🤖 Maintained by @T3chieJack
yaml
Copy
Edit

---

## ✅ Final Checklist

| Task | Status |
|------|--------|
| `.github/workflows/scrape.yml` exists and contains valid YAML | ✅ |
| `scraper.py` runs without error | ✅ |
| `requirements.txt` includes `playwright` | ✅ |
| Workflow permissions are set to **read/write** in repo settings | ✅ |
| Manually triggered the first workflow | 🔜 |
| Added README badge | ✅ |
| Added fancy README description | ✅ |

---

Would you like me to:
- Check your public repo and verify the workflow path?
- Add CSV/Markdown exports?
- Help you build a GitHub Pages UI that reads the prices?

Let me know!
