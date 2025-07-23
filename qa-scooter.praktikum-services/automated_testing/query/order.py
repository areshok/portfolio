import json
import allure

from .base import BaseRequest

from automated_testing.data.urls import URLS


class OrderRequest(BaseRequest):

    class ResponseField:
        err = "message"
        get = "order"

    class ResponseText:
        accept_order_missing = "Недостаточно данных для поиска"
        courier_non_exist = "Курьера с таким id не существует"
        order_non_exists = "Заказа с таким id не существует"
        order_null = "Недостаточно данных для поиска"
        non_exists_track = "Заказ не найден"

    @allure.step("Создание заказа")
    def create(self, data):
        headers = {
            "Content-Type": "application/json"
        }
        response = self.post(
            url=URLS["api"]["order"]["create"],
            data=json.dumps(data),
            headers=headers
        )
        return self.result_json(response)

    @allure.step("Получение списка заказов")
    def list(self):
        response = self.get(url=URLS["api"]["order"]["list"])
        return self.result_json(response)

    @allure.step("Принятие заказа")
    def accept_order(self, id_order, id_courier):
        url = f'{URLS["api"]["order"]["accept"]}{id_order}?courierId={id_courier}'
        response = self.put(url=url)
        result = self.result_json(response)
        return result

    @allure.step("Получить информацию о заказе")
    def get_order(self, track_order):
        url = f'{URLS["api"]["order"]["get"]}?t={track_order}'
        response = self.get(url=url)
        return self.result_json(response)
