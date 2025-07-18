import requests
import allure


class BaseRequest:

    @allure.step("Преобразование тела ответа в json")
    def result_json(self, response):
        status = self.status_code(response)
        try:
            body = response.json()
        except Exception:
            body = None
        return {
            "status": status,
            "body": body
        }

    @allure.step("Отправка POST запроса")
    def post(self, *args, **kwargs):
        return requests.post(*args, **kwargs)

    @allure.step("Отправка GET запроса")
    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs)

    @allure.step("Получаем код статуса")
    def status_code(self, response):
        return response.status_code
