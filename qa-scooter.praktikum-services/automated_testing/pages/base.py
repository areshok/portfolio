import platform
import time

import allure
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException, NoSuchElementException)

OS = platform.system()
TIME_MAX = 10


class BasePage:
    def __init__(self, browser):
        self.__browser = browser

    def __define_os(self, field):
        if OS == "Windows" or OS == "Linux":
            self.__clean_win_uix(field)
        if OS == "Darwin":
            self.__clean_mac_os(field)

    def __clean_mac_os(self, field):
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)

    def __clean_win_uix(self, field):
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)

    @allure.step("Очистка поля")
    def clear_field(self, field):
        self.__define_os(field)

    @allure.step("Прокрутка до элемента")
    def scrol_to_element(self, element):
        self.__browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание получения элемента")
    def get_element(self, path):
        "Ожидание элемента"
        time_start = time.time()
        while True:
            try:
                element = self.__browser.find_element(*path)
                return element
            except NoSuchElementException as e:
                if time.time() - time_start > TIME_MAX:
                    raise e
                time.sleep(0.5)

    @allure.step("Ожидание получение кнопки и нажатия")
    def get_button_click(self, path=None, element=None):
        "Ожидание нажатия"
        time_start = time.time()
        if element is None:
            button = self.get_element(path)
        else:
            button = element
        while True:
            try:
                button.click()
                return button
            except ElementClickInterceptedException as e:
                if time.time() - time_start > TIME_MAX:
                    raise e
                time.sleep(0.5)

    @allure.step("Открытие url")
    def open_url(self, url):
        self.__browser.get(url)

    @allure.step("Получаем текущий url")
    def current_url(self):
        return self.__browser.current_url

    @allure.step("Меняем активную вкладку браузера")
    def change_the_window(self, number_window):
        new_window = self.__browser.window_handles[number_window]
        self.__browser.switch_to.window(new_window)
