import allure

from stellarburgers.pages.constructor_page import ConstructorPage
from stellarburgers.pages.feed_page import FeedPage
from stellarburgers.data.urls import URLS


class TestCaseFeed:

    @allure.title(
        """
        тест: при создании нового заказа счётчик «Выполнено за всё время»
        увеличивается
        тест: при создании нового заказа счётчик «Выполнено за сегодня»
        увеличивается
        тест: после оформления заказа его номер появляется в разделе «В работе
        """
    )
    def test_after_create_order_feed_page(
            self,
            auth_browser):
        """
        тест: при создании нового заказа счётчик
        «Выполнено за всё время» увеличивается
        тест: при создании нового заказа счётчик
        «Выполнено за сегодня» увеличивается
        тест: после оформления заказа его номер появляется в разделе «В работе
        """
        feed = FeedPage(auth_browser)
        constructor = ConstructorPage(auth_browser)
        feed.open_url(URLS["ui"]["/"])
        feed.open_url(URLS["ui"]["feed"])
        in_day = feed.get_complited_in_day()
        all_time = feed.get_complited_in_all_time()
        constructor.open_url(URLS["ui"]["/"])
        constructor.create_order()
        order = constructor.get_nuber_order()
        constructor.close_confirm_window()
        feed.open_url(URLS["ui"]["feed"])
        numbers = feed.get_numbe_orders_in_work(order)
        in_day_after_order = feed.get_complited_in_day()
        all_time_after_order = feed.get_complited_in_all_time()
        assert order in numbers
        assert in_day < in_day_after_order
        assert all_time < all_time_after_order
