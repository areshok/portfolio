import allure

from ..locators.header import HeaderLocator
from .base import BasePage


class HeaderPage(BasePage):

    @allure.step("Нажимаем на логотип Yandex")
    def click_yandex_logo(self):
        self.get_button_click(path=HeaderLocator.yandex)

    @allure.step("Нажимаем на логотип Самокат")
    def click_scooter_logo(self):
        self.get_button_click(path=HeaderLocator.scooter)

    @allure.step("Нажимаем на кнопку Заказать")
    def click_order(self):
        self.get_button_click(path=HeaderLocator.order)
