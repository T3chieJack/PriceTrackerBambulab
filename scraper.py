from playwright.sync_api import sync_playwright
import json

URL = "https://uk.store.bambulab.com/products/pla-basic-filament"

def scrape_bambu_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.wait_for_selector("div.grid-product__title")

        product_titles = page.query_selector_all("div.grid-product__title")
        product_prices = page.query_selector_all("div.grid-product__price span")

        products = []
        for title, price in zip(product_titles, product_prices):
            products.append({
                "title": title.inner_text().strip(),
                "price": price.inner_text().strip()
            })

        browser.close()
        return products

if __name__ == "__main__":
    prices = scrape_bambu_prices()
    with open("prices.json", "w") as f:
        json.dump(prices, f, indent=2)
    print("Scraped and saved prices to prices.json")

