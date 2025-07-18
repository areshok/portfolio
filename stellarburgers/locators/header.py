
from selenium.webdriver.common.by import By


class Header:
    invisabilati = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")
    constuctor = (By.XPATH, ".//a[p[text()='Конструктор']]")
    order_feed = (By.XPATH, ".//a[p[text()='Лента Заказов']]")
    logo = (
        By.XPATH,
        ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")
    personal_account = (By.XPATH, ".//a[p[text()='Личный Кабинет']]")
