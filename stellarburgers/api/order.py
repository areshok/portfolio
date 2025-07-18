import random

import allure

from .base import BaseRequest
from ..data.urls import URLS


class OrderReauest(BaseRequest):

    class ResposeText:
        empty_ingridients = "Ingredient ids must be provided"

    @allure.step("Получение списка ингридиентов")
    def ingridients(self, *args, **kwargs):
        response = self.get(url=URLS["api"]["ingridients"], *args, **kwargs)
        result = self.result_json(response)
        return result

    @allure.step("Создание заказа")
    def create(self, *args, **kwargs):
        response = self.post(url=URLS["api"]["order"], *args, **kwargs)
        result = self.result_json(response)
        return result

    @allure.step("Получение случайного списка ингридиентов")
    def get_random_ingridients(self):
        response = self.ingridients()
        hash_ingridients = []
        result_hash_ingridients = []
        for element in response["body"]["data"]:
            hash_ingridients.append(element["_id"])
        count_ingridients = len(hash_ingridients)
        result_count_ingridients = random.randint(0, count_ingridients)
        for _ in range(result_count_ingridients):
            result_hash_ingridients.append(random.choice(hash_ingridients))
        return {"ingredients": result_hash_ingridients}
