import datetime
import random
import string
from random import choice

import allure

from .settings import LENGTH_GENERATE

stations = [
    "Сокольники",
    "Красносельская",
    "Комсомольская",
    "Проспект Мира",
    "Новослободская",
    "Тверская",
    "Библиотека им. Ленина",
    "Парк культуры",
    "Фрунзенская",
    "Спортивная",
    "Киевская",
    "Кутузовская",
    "Студенческая",
    "Краснопресненская",
    "Алма-Атинская",
    "Дубровка",
    "Кожуховская",
    "Печатники",
    "Волжская",
    "Люблино"
]

colors = ["BLACK", "GREY", "BLACK, GREY", ""]


@allure.step("Получаем завтрашнюю дату")
def get_tomorrow_day():
    "Возвращяет завтрашную дату"
    return str((datetime.date.today() + datetime.timedelta(days=1)
                ).strftime("%d.%m.%Y"))


@allure.step("Генерация строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step("генерация пользователя")
def generate_user(length=LENGTH_GENERATE):
    name = generate_random_string(length)
    password = generate_random_string(length)
    firstname = generate_random_string(length)
    return {
        "firstname": firstname,
        "password": password,
        "login": name
    }


def generate_order(length=LENGTH_GENERATE):
    def generate_metroStation():
        return choice(stations)

    def generate_phone():
        phone = "+7"
        for _ in range(10):
            digit = choice(string.digits)
            phone += digit
        return phone

    def generate_renttime():
        while True:
            digit = int(choice(string.digits))
            if digit != 0:
                return digit

    def generate_date():
        date = (datetime.date.today() + datetime.timedelta(days=1))\
            .strftime("%Y-%m-%d")
        return date

    data = {
        "firstname": generate_random_string(length),
        "lastname": generate_random_string(length),
        "address": generate_random_string(length),
        "metroStation": generate_metroStation(),
        "phone": generate_phone(),
        "rentTime": generate_renttime(),
        "deliveryDate": generate_date(),
        "comment": generate_random_string(length),
    }

    return data
