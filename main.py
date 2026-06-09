import threading

from fastapi import FastAPI
from dotenv import load_dotenv
import os
import scheduler
from naukri import apply_jobs, auto_apply_loop

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")

@app.get("/")
def home():
    return {
    "message": "API Working"
    }

@app.get("/apply-jobs")
def run_apply_jobs():

    result = apply_jobs()

    return result
@app.get("/start-auto-apply")
def start_auto_apply():
    thread = threading.Thread(
        target=auto_apply_loop
    )

    thread.start()

    return {
        "message": "Auto apply started"
    }

