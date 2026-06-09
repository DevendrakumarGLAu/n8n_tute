from playwright.sync_api import sync_playwright
import time

def apply_single_job():
    print("Applying one job")

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

        time.sleep(5)

        # APPLY LOGIC HERE

        browser.close()

    print("Job Applied")

def refresh_profile():

    print("Refreshing profile")

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

        time.sleep(5)

        # REFRESH PROFILE LOGIC

        browser.close()

    print("Profile Refreshed")


def update_application_status():

    print("Updating status")

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

        time.sleep(5)

        # STATUS UPDATE LOGIC

        browser.close()

    print("Status Updated")
