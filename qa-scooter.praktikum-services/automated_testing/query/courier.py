import allure

from .base import BaseRequest
from automated_testing.data.urls import URLS


class CourierRequest(BaseRequest):
    class ResponseField:
        login = "id"
        err = "message"
        create = "ok"

    class ResponseText:
        dublicat_user = "Этот логин уже используется"
        missing_field_register = "Недостаточно данных для создания учетной записи"
        missing_field_login = "Недостаточно данных для входа"
        non_existent = "Учетная запись не найдена"
        non_existent_delete = "Курьера с таким id нет."
        missing_id_delete = "Недостаточно данных для удаления курьера"

    @allure.step("Регистрация курьера")
    def register(self, login=None, password=None, firstname=None):
        data = {}
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        if firstname is not None:
            data["firstname"] = firstname
        response = self.post(url=URLS["api"]["courier"]["create"], data=data)
        return self.result_json(response)

    @allure.step("Авторизиция курьера")
    def login(self, login=None, password=None):
        data = {}
        if login is not None:
            data["login"] = login
        if password is not None:
            data["password"] = password
        response = self.post(url=URLS["api"]["courier"]["login"], data=data)
        return self.result_json(response)

    @allure.step("Удаление курьера")
    def delete_courier(self, id_courier):
        url = f'{URLS["api"]["courier"]["delete"]}{id_courier}'
        response = self.delete(
            url=url,
        )
        return self.result_json(response)
