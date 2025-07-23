import allure

#from ..urls.urls import URLS
#from ..pages.order_page import OrderPageOne, OrderPageTwo
#from ..pages.home_page import HomePage
#from ..locators.order import PageConfirmLocator
#from ..locators.header import HeaderLocator
#from ..data.form import DataOrderForm

from automated_testing.data.urls import URLS
from automated_testing.pages.order_page import OrderPageOne, OrderPageTwo
from automated_testing.pages.home_page import HomePage
from automated_testing.locators.order import PageConfirmLocator
from automated_testing.locators.header import HeaderLocator
from automated_testing.data.form import DataOrderForm


class TestOrderCase:
    "Тест кейс бронирования самоката"

    @allure.title("""Тест: бронирование самоката,
                нажатием на кнопку в шапке странице""")
    def test_order_rus_first_last_name_button_header(self, browser_def):
        """тест: бронирование самоката, нажатием на кнопку в шапке странице"""
        data = DataOrderForm.get_data()
        order = OrderPageOne(browser_def)
        order.open_url(URLS["ui"]['/'])
        order.get_button_click(path=HeaderLocator.order)
        order.complete_form(**data['page_one'])
        order = OrderPageTwo(browser_def)
        order.complete_form(**data['page_two'])
        status = order.return_status_order()
        assert PageConfirmLocator.text in status

    @allure.title("""Тест: бронирование самоката,
                нажатием на кнопку на главной странице,с новыми данными""")
    def test_order_end_first_last_name_button_home_page(self, browser_def):
        """
        тест: бронирование самоката, нажатием на кнопку на главной странице,
        с новыми данными
        """
        home = HomePage(browser_def)
        home.open_url(URLS["ui"]['/'])
        home.scrol_button_order_click()
        data = DataOrderForm.get_new_data()
        order = OrderPageOne(browser_def)
        order.complete_form(**data['page_one'])
        order = OrderPageTwo(browser_def)
        order.complete_form(**data['page_two'])
        status = order.return_status_order()
        assert PageConfirmLocator.text in status
