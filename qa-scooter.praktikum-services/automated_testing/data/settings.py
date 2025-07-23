import os
from pathlib import Path

from selenium import webdriver

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = os.path.join(BASE_DIR, "data/created_users.csv")
CHECK_USER_FILE = os.path.exists(USERS_FILE)

LENGTH_GENERATE = 10

CREATED_COURIER = {
    "login": "arstest",
    "password": "Arstest1",
    }


def get_courier():
    return CREATED_COURIER


def get_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    browser = webdriver.Firefox(options=options)
    return browser
