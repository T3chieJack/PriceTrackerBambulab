from playwright.sync_api import sync_playwright
import json

def scrape_bambu_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://uk.store.bambulab.com/collections/bambu-lab-3d-printer-filament")

        # Wait for products to load (adjusted selector)
        page.wait_for_selector("div.product-item-meta")

        product_elements = page.query_selector_all("div.product-item-meta")

        prices = []
        for product in product_elements:
            title_el = product.query_selector("div.product-title a")
            price_el = product.query_selector("span.price")

            title = title_el.inner_text().strip() if title_el else "Unknown"
            price = price_el.inner_text().strip() if price_el else "N/A"

            prices.append({
                "title": title,
                "price": price
            })

        browser.close()
        return prices

if __name__ == "__main__":
    prices = scrape_bambu_prices()

    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
