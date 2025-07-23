from selenium.webdriver.common.by import By


class DzenLocator:
    input_field = (By.XPATH, ".//input[@class='arrow__input mini-suggest__input']")
    search = (By.XPATH, ".//button[text()='Найти']")
