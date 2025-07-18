
from selenium.webdriver.common.by import By


class FeedLocator:
    in_work = (
        By.XPATH,
        ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    finished = (By.XPATH, ".//ul[@class='OrderFeed_orderList__cBvyi']")
    element = (By.XPATH, ".//li")
    complited_in_all_time = (
        By.XPATH,
        ".//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    complited_in_day = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    order = (
        By.XPATH,
        ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[text()='{}']")
