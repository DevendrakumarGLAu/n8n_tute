from playwright.sync_api import sync_playwright
import os
import time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

def update_status():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page()

        page.goto("https://www.naukri.com")

        time.sleep(3)

        page.click("text=Login")

        page.fill('input[type="text"]', EMAIL)
        page.fill('input[type="password"]', PASSWORD)

        page.click('button[type="submit"]')

        time.sleep(5)

        page.goto("https://www.naukri.com/mnjuser/recommendedjobs")

        time.sleep(5)

        print("Status updated")

        browser.close()


    update_status()
