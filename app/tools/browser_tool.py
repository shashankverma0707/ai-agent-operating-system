from playwright.sync_api import sync_playwright


def open_website(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url)

        title = page.title()

        browser.close()

        return title