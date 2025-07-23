from selenium.webdriver.common.by import By


class HeaderLocator:
    yandex = (By.XPATH, ".//a[@href='//yandex.ru']")
    scooter = (By.XPATH, ".//a[@href='/']")
    order = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    status = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Статус заказа']")
    search = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    button_go = (By.XPATH, ".//button[text()='Go!']")
