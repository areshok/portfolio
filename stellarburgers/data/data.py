import random
import string

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .settings import LENGHT_GENERATE


USER = {"login": "ars@ars.ru", "password": "123456"}

hash_ingridient = {"ingredients": ["00000000000000000000000"]}

@allure.step("Генерация строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("генерация email")
def generate_email(name):
    domains = ["@mail.ru", "@yandex.ru", "@google.com"]
    email = name + random.choice(domains)
    return email


@allure.step("генерация пользователя")
def generate_user(length=LENGHT_GENERATE):
    name = generate_random_string(length)
    password = generate_random_string(length)
    email = generate_email(name)
    return {
        "email": email,
        "password": password,
        "name": name
    }

@allure.step("Октрытие браузера {name_browser}")
def get_browser(name_browser):
    if name_browser == "chrome":
        options = Options()
        options.add_argument("--disable-cache")
        options.add_argument("--incognito")
        browser = webdriver.Chrome(options=options)
    elif name_browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--private")
        browser = webdriver.Firefox(
            options=options
                )
    return browser
