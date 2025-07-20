import sys
from pathlib import Path

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .data.data import generate_user, hash_ingridient
from .data.urls import URLS
from .pages.user_page import UserPage
from .data.data import USER, get_browser


ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))


@pytest.fixture(params=[
    "chrome",
    "firefox"
    ])
def browser(request):
    browser = get_browser(request.param)
    browser.get(URLS["ui"]["/"])
    yield browser
    browser.quit()


@pytest.fixture(params=[
    "chrome",
    "firefox"
    ],
    scope="class")
def browser_cls(request):
    browser = get_browser(request.param)
    browser.get(URLS["ui"]["/"])
    yield browser
    browser.quit()


@pytest.fixture()
def auth_browser(browser):
    user = UserPage(browser)
    user.login(**USER)
    return browser


@pytest.fixture(scope="function")
@allure.step("Получаем пользователя для функции")
def user_def():
    return generate_user()


@pytest.fixture(scope="class")
@allure.step("Получаем пользователя для класса")
def user_cls():
    return generate_user()


@pytest.fixture(scope="function")
@allure.step("Получаем некорректный хеш ингридиента")
def uncorrect_hash_ingridient():
    return hash_ingridient
