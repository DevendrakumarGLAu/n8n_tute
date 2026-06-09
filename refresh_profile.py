from playwright.sync_api import sync_playwright
import os
import time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

def refresh_profile():

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

        time.sleep(2)

        page.fill('input[type="text"]', EMAIL)
        page.fill('input[type="password"]', PASSWORD)

        page.click('button[type="submit"]')

        time.sleep(5)

        # OPEN PROFILE
        page.goto("https://www.naukri.com/mnjuser/profile")

        time.sleep(5)

        # CLICK SAVE BUTTON
        save_buttons = page.locator("button")

        count = save_buttons.count()

        for i in range(count):

            try:

                btn = save_buttons.nth(i)

                text_value = btn.inner_text()

                if "Save" in text_value:

                    btn.click()

                    break

            except:
                pass

        print("Profile refreshed")

        browser.close()

    refresh_profile()