import allure

from .base import BasePage
from ..locators.header import Header


class HeaderPage(BasePage):

    @allure.step("Нажатие на кнопку 'Конструктор' в шапке сайта")
    def click_constructor(self):
        self.click(Header.constuctor)

    @allure.step("Нажатие на кнопку 'Лента заказов' в шапке сайта")
    def click_order_feed(self):
        self.click(Header.order_feed)
