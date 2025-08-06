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
