from selenium.webdriver.common.keys import Keys
import allure

from .base import BasePage

from ..locators.order import PageOneLocator, PageTwoLocator, PageConfirmLocator


class OrderPageOne(BasePage):

    @allure.step("Заполняем поле Имя")
    def write_first_name(self, fname):
        field = self.get_element(PageOneLocator.first_name)
        field.send_keys(fname)

    @allure.step("Заполняем поле Фамилия")
    def write_last_name(self, lname):
        field = self.get_element(PageOneLocator.last_name)
        field.send_keys(lname)

    @allure.step("Заполняем поле Адрес")
    def write_address(self, address):
        field = self.get_element(PageOneLocator.address)
        field.send_keys(address)

    @allure.step("Выбираем станцию метро в поле Станция")
    def choise_metro_stantion(self, metro):
        update_xpath = PageOneLocator.station[1].format(metro.strip())
        new_locator = (PageOneLocator.station[0], update_xpath)
        self.get_button_click(path=PageOneLocator.metro)
        station = self.get_element(new_locator)
        self.scrol_to_element(station)
        self.get_button_click(element=station)

    @allure.step("Заполняем поле Телефон")
    def write_telephon(self, phone):
        field = self.get_element(PageOneLocator.phone)
        field.send_keys(phone)

    @allure.step("Нажимаем кнопку Далее")
    def enter_button_form(self):
        self.get_button_click(path=PageOneLocator.button)

    @allure.step("Заполняем форму бронирования самоката, превая страница")
    def complete_form(self, fname, lname, address, metro, phone):
        self.write_first_name(fname)
        self.write_last_name(lname)
        self.write_address(address)
        self.choise_metro_stantion(metro)
        self.write_telephon(phone)
        self.enter_button_form()

    @allure.step("Очищаем поле Имя")
    def clean_first_name(self):
        field = self.get_element(PageOneLocator.first_name)
        self.clear_field(field)

    @allure.step("Очищаем поле Фамилия")
    def clean_last_name(self):
        field = self.get_element(PageOneLocator.last_name)
        self.clear_field(field)

    @allure.step("Очищаем поле Адрес")
    def clean_address(self):
        field = self.get_element(PageOneLocator.address)
        self.clear_field(field)

    @allure.step("Очищаем поле Телефон")
    def clean_telephon_nubmer(self):
        field = self.get_element(PageOneLocator.phone)
        self.clear_field(field)

    @allure.step("Очищаем форму бронирования самоката, превая страница")
    def clean_form(self):
        self.clean_first_name()
        self.clean_last_name()
        self.clean_address()
        self.clean_telephon_nubmer()


class OrderPageTwo(BasePage):

    @allure.step("Выбираем дату")
    def choise_date(self, date):
        field = self.get_element(PageTwoLocator.date)
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step("Выбараем срок аренды")
    def choise_rent(self, rend_day):
        self.get_button_click(path=PageTwoLocator.rent)
        update_locator = PageTwoLocator.day[1].format(rend_day.strip())
        new_locator = (PageTwoLocator.day[0], update_locator)
        day = self.get_element(new_locator)
        self.scrol_to_element(day)
        day.click()

    @allure.step("Выбираем цвет")
    def choise_color(self, color):
        update_locator = PageTwoLocator.checkbox[1].format(color.strip())
        new_locator = (PageTwoLocator.checkbox[0], update_locator)
        self.get_button_click(path=new_locator)

    @allure.step("Заполняем поле Комментарий")
    def write_comment(self, comment):
        field = self.get_element(PageTwoLocator.comment)
        field.send_keys(comment)

    @allure.step("Нажимаем на кнопку Далее")
    def enter_button_form(self):
        self.get_button_click(path=PageTwoLocator.order)

    @allure.step("Нажимаем на кнопку Назад")
    def back_button_form(self):
        self.get_button_click(path=PageTwoLocator.back)

    @allure.step("Нажимаем на кнопку подтвердить")
    def confirm(self):
        self.get_button_click(path=PageConfirmLocator.yes)

    @allure.step("Получаем результат бронирования самоката")
    def return_status_order(self):
        text = self.get_element(PageConfirmLocator.order).text
        return text

    @allure.step("Заполняем форму бронирования самоката, вторая страница")
    def complete_form(self, date, rend_day, color, comment):
        self.choise_date(date)
        self.choise_rent(rend_day)
        self.choise_color(color)
        self.write_comment(comment)
        self.enter_button_form()
        self.confirm()
