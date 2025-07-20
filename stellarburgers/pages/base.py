import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from ..locators.invisible_window import InvisibleLocator


TIME_MAX = 100


class BasePage:

    def __init__(self, browser):
        self.__browser = browser
        self.__wait = WebDriverWait(self.__browser, TIME_MAX)

    @allure.step("Открытие url")
    def open_url(self, url):
        self.__browser.get(url)

    @allure.step("Получаем текущий url")
    def current_url(self):
        return self.__browser.current_url

    @allure.step("Прокрутка до элемента")
    def scrol_to_element(self, element):
        self.__browser.execute_script(
            "arguments[0].scrollIntoView();", element)

    @allure.step("Перетаскивание элемента")
    def drag_and_drop_seletools(self, source, target):
        drag_and_drop(self.__browser, source, target)

    @allure.step("Ввод текста в поле")
    def write_field(self, field, text):
        field.send_keys(text)

    @allure.step("Получение элемента")
    def get_element(self, path):
        "Получение элемента"
        return self.__wait.until(EC.presence_of_element_located(path))

    @allure.step("Получение элементов")
    def get_elements(self, path):
        "Получение элементов"
        return self.__wait.until(EC.visibility_of_all_elements_located(path))

    @allure.step("Нажимаем кнопку. Путь")
    def click(self, path):
        "Нажать на кноку"
        self.wait_invisible_window(InvisibleLocator.window_1)
        self.wait_invisible_window(InvisibleLocator.window_2)
        self.wait_invisible_window(InvisibleLocator.window_3)
        self.__wait.until(EC.element_to_be_clickable(path))
        button = self.get_element(path)
        button.click()
        return button

    @allure.step("Нажимаем кнопку. Элемент")
    def click_element(self, element):
        self.wait_invisible_window(InvisibleLocator.window_1)
        self.wait_invisible_window(InvisibleLocator.window_2)
        self.wait_invisible_window(InvisibleLocator.window_3)
        self.__wait.until(EC.element_to_be_clickable(element))
        element.click()
        return element

    @allure.step("Ожидание пропадания невидимого окна")
    def wait_invisible_window(self, path):
        self.__wait.until(EC.invisibility_of_element(path))

    @allure.step("Ожидание появление элемента")
    def wait_element_in_visible(self, path):
        self.__wait.until(EC.visibility_of_element_located(path))

    def wait_change_class(self, section, element):
        self.__wait.until(lambda d: section in element.get_attribute('class'))
