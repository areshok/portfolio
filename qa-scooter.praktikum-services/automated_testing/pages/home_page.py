import allure

from ..locators.home import HomeLocator
from .base import BasePage


class HomePage(BasePage):

    @allure.step("Прокрутка до кнопки заказад на домашней странице")
    def scrol_button_order_click(self):
        button = self.get_element(HomeLocator.order)
        self.scrol_to_element(button)
        self.get_button_click(element=button)


class QuestionPage(BasePage):

    @allure.step("Получаем атрибут hidden у элемента ответа")
    def answer_status_hidden(self, element):
        status = element.get_attribute(HomeLocator.Question.status_answer)
        return status

    @allure.step("Получаем вопрос")
    def get_question(self, count):
        update_xpath = HomeLocator.Question.question_xpath_pattern[1].format(count)
        new_path = (
            HomeLocator.Question.question_xpath_pattern[0],
            update_xpath
        )
        element = self.get_element(new_path)
        return element

    @allure.step("Получаем ответ")
    def get_answer(self, count):
        update_xpath = HomeLocator.Question.answer_xpath_pattern_question[1].format(count, count)
        new_path = (
            HomeLocator.Question.answer_xpath_pattern_question[0],
            update_xpath)
        element = self.get_element(new_path)
        return element
