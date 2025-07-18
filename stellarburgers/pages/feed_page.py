import allure

from .base import BasePage
from ..locators.feed import FeedLocator


class FeedPage(BasePage):

    @allure.step("Получение списка заказов в работе")
    def get_numbe_orders_in_work(self, order):
        order_locator = (
            FeedLocator.order[0], FeedLocator.order[1].format(order))
        self.wait_element_in_visible(order_locator)
        block = self.get_element(FeedLocator.in_work)
        elements = block.find_elements(*FeedLocator.element)
        numbers = []
        for element in elements:
            numbers.append(int(element.text))
        return numbers

    @allure.step("Получение количества заказов за все время")
    def get_complited_in_all_time(self):
        return int(self.get_element(FeedLocator.complited_in_all_time).text)

    @allure.step("Получение количество заказов за день")
    def get_complited_in_day(self):
        return int(self.get_element(FeedLocator.complited_in_day).text)
