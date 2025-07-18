import allure

from .base import BasePage
from ..locators.user import UserLocator
from ..locators.constructor import Designer
from ..data.urls import URLS


class UserPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login(self, login, password):
        self.open_url(URLS["ui"]["login"])
        field = self.get_element(UserLocator.LoginPage.email)
        self.write_field(field, login)
        field = self.get_element(UserLocator.LoginPage.password)
        self.write_field(field, password)
        self.click(UserLocator.LoginPage.enter)
        self.check_login_user()

    @allure.step("Проверка что пользователь вошел на сайт")
    def check_login_user(self):
        self.get_element(Designer.order)
