from fastapi import FastAPI
from dotenv import load_dotenv
import os

from naukri import apply_jobs

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

