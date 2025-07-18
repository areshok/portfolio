import allure

from .base import BaseRequest
from ..data.urls import URLS


class UserRequest(BaseRequest):

    class ResponseText:
        dublicate = "User already exists"
        missing_field_register = "Email, password and name are required fields"
        uncorrect_field = "email or password are incorrect"

    def __init__(self):
        self.__token = None
        self.__refresh_token = None

    @property
    @allure.step("получение тока")
    def token(self):
        return self.__token

    @property
    @allure.step("получение токена обновления")
    def refresh_token(self):
        return self.__refresh_token

    @allure.step("Регистрация пользователя")
    def register(self, *args, **kwargs):
        response = self.post(url=URLS["api"]["register"], *args, **kwargs)
        result = self.result_json(response)
        if result["body"]["success"]:
            self.__update_token(result["body"])
        return result

    @allure.step("Авторизация пользователя")
    def login(self, *args, **kwargs):
        response = self.post(url=URLS["api"]["login"], *args, **kwargs)
        result = self.result_json(response)
        return result

    @allure.step("Сохранение токенов в переменных")
    def __update_token(self, body):
        self.__token = body["accessToken"]
        self.__refresh_token = body["refreshToken"]
