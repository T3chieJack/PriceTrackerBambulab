from playwright.sync_api import sync_playwright
import json
import time

def scrape_bambu_prices():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://uk.store.bambulab.com/collections/bambu-lab-3d-printer-filament", timeout=60000)

        # Wait for product items (anchor tags)
        page.wait_for_selector("a.product-item", timeout=60000)

        # Scroll down to ensure lazy loading if any
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)

        products = page.locator("a.product-item")
        count = products.count()
        items = []

        for i in range(count):
            product = products.nth(i)
            title = product.locator("p.product-title").inner_text()
            price = product.locator("span.price").inner_text()
            items.append({"title": title.strip(), "price": price.strip()})

        # Optional: Save a screenshot for debugging
        page.screenshot(path="debug_screenshot.png")

        browser.close()
        return items

if __name__ == "__main__":
    prices = scrape_bambu_prices()
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)
