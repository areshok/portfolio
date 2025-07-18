import allure

from stellarburgers.pages.header_page import HeaderPage
from stellarburgers.pages.constructor_page import ConstructorPage
from stellarburgers.data.urls import URLS
from stellarburgers.locators.constructor import Detail


class TestCaseBasicFunctionality:

    @allure.title("тест: переход по клику на «Конструктор»")
    def test_click_through_to_constructor(self, browser):
        "тест: переход по клику на «Конструктор»"
        header = HeaderPage(browser)
        header.open_url(URLS["ui"]["feed"])
        header.click_constructor()
        current_url = header.current_url()
        assert current_url == URLS["ui"]["/"]

    @allure.title("тест: переход по клику на раздел «Лента заказов»")
    def test_click_through_to_the_order_feed(self, browser):
        "тест: переход по клику на раздел «Лента заказов»"
        header = HeaderPage(browser)
        header.click_order_feed()
        current_url = header.current_url()
        assert current_url == URLS["ui"]["feed"]

    @allure.title("тест: при клике на ингредиент октрывется окно с деталями")
    def test_click_on_an_ingredien_open_window_details(self, browser):
        "тест: при клике на ингредиент октрывется окно с деталями"
        constructor = ConstructorPage(browser)
        ingridient = constructor.get_first_topping()
        result = constructor.click_ingridient(ingridient)
        assert Detail.name_text == result["heading"]
        assert result["description"] in result["element"]

    @allure.title(
        "тест: закрытие окна с деталями ингредиента при нажатии на крест"
    )
    def test_close_detail_window_press_button(self, browser):
        "тест: закрытие окна с деталями ингредиента при нажатии на крест"
        constructor = ConstructorPage(browser)
        ingridient = constructor.get_first_topping()
        constructor.click_ingridient(ingridient)
        constructor.close_detail_window()
        result = constructor.class_detail_window()
        assert Detail.open not in result

    @allure.title(
        """
        тест: при добавлении ингредиента в заказ счётчик
        этого ингредиента увеличивается
        """
    )
    def test_drag_and_drop_ingridients(self, browser):
        """
        тест: при добавлении ингредиента в заказ счётчик
        этого ингредиента увеличивается
        """
        constructor = ConstructorPage(browser)
        element = constructor.get_first_topping()
        constructor.drag_and_drop_ingredient(element)
        count = int(constructor.count_ingridient(element))
        assert count == 1
