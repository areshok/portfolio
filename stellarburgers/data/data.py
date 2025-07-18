import random
import string

import allure

from ..settings import LENGHT_GENERATE


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