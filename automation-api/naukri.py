# automation-api\main.py

from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()

NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

def apply_jobs():
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

        print("Opened Naukri")

        # Login logic here

        browser.close()

    return {
        "status": "success"
    }
    # ```
