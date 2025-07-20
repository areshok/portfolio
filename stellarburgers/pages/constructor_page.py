import allure

from .base import BasePage
from ..locators.constructor import Designer, Detail, Confirm, Ingridient
from ..locators.invisible_window import InvisibleLocator


class ConstructorPage(BasePage):

    @allure.step("Получение первого топпинга")
    def get_first_topping(self):
        element = self.get_element(Ingridient.topping_first)
        return element

    @allure.step("Нажатие на ингридиент")
    def click_ingridient(self, element):
        self.scrol_to_element(element)
        self.click_element(element)
        window = self.get_detail_window()
        window["element"] = element.text
        return window

    @allure.step("Получение информации окно 'О ингридиенте'")
    def get_detail_window(self):
        window = self.get_element(Detail.window)
        heading = window.find_element(*Detail.heading_in_window).text
        description = window.find_element(
            *Detail.description_in_window).text
        return {"heading": heading, "description": description}

    @allure.step("Закрываем окно 'О ингридиенте'")
    def close_detail_window(self):
        self.click(Detail.button)

    @allure.step("Получение class элемента section окна 'О ингридиенте'")
    def class_detail_window(self) -> str:
        element = self.get_element(Detail.parent_window)
        return element.get_attribute("class")

    @allure.step("Перетаскивание ингридиента")
    def drag_and_drop_ingredient(self, element):
        basket = self.get_element(path=Designer.basket_area)
        self.scrol_to_element(element)
        self.drag_and_drop_seletools(element, basket)

    @allure.step("Получаем количество ингридиента")
    def count_ingridient(self, element):
        return element.find_element(
            *Designer.count_ingridient).text

    @allure.step("Нажимаем на кноку сделать заказ")
    def click_button_order(self):
        self.click(Designer.order)

    @allure.step("Создаем заказ")
    def create_order(self):
        bread = self.get_element(Ingridient.bread_first)
        souce = self.get_element(Ingridient.souce_first)
        topping = self.get_element(Ingridient.topping_first)
        self.drag_and_drop_ingredient(bread)
        self.drag_and_drop_ingredient(souce)
        self.drag_and_drop_ingredient(topping)
        self.click_button_order()

    @allure.step("Получаем номер заказа")
    def get_nuber_order(self):
        self.wait_invisible_window(InvisibleLocator.window_3)
        number = self.get_element(Confirm.number)
        return int(number.text)

    @allure.step("Закрываем окно подтверждение закза")
    def close_confirm_window(self):
        self.click(Confirm.exit)
