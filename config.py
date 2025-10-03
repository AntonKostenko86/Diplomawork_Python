# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = "https://www.kinopoisk.ru/"
    API_URL = "https://api.kinopoisk.dev"
    API_TOKEN = os.getenv("API_TOKEN", "")
    WAIT_TIMEOUT = 50
    IMPLICIT_WAIT = 10