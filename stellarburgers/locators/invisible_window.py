
from selenium.webdriver.common.by import By


class InvisibleLocator:
    window_1 = (
        By.XPATH,
        ".//section[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']")
    window_2 = (
        By.XPATH,
        ".//div[@class='Modal_modal__P3_V5']/div[@class='Modal_modal_overlay__x2ZCr']")
    window_3 = (
        By.XPATH,
        ".//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
