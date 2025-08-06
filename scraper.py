from playwright.sync_api import sync_playwright
import json
import time

def scrape_bambu_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://uk.store.bambulab.com/collections/bambu-lab-3d-printer-filament", timeout=60000)

        # Wait until the product grid is loaded
        page.wait_for_selector("product-item", timeout=60000)

        # Scroll down to load lazy-loaded items
        page.evaluate("""() => {
            window.scrollTo(0, document.body.scrollHeight);
        }""")
        time.sleep(3)  # Allow extra content to load

        products = page.locator("product-item")

        items = []
        count = products.count()

        for i in range(count):
            title = products.nth(i).locator("p.product-title").inner_text()
            price = products.nth(i).locator("span.price").inner_text()
            items.append({"title": title.strip(), "price": price.strip()})

        browser.close()

        return items

# Save the scraped data to a JSON file
prices = scrape_bambu_prices()
with open("prices.json", "w", encoding="utf-8") as f:
    json.dump(prices, f, indent=2, ensure_ascii=False)
