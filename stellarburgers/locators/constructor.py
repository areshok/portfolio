
from selenium.webdriver.common.by import By


class Designer:
    breads = (By.XPATH, ".//span[text()='Булки']")
    parents_bread = (By.XPATH, ".//span[text()='Булки']/parent::div")
    sauces = (By.XPATH, ".//span[text()='Соусы']")
    parent_sauces = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    toppings = (By.XPATH, ".//span[text()='Начинки']")
    parent_toppings = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    basket_area = (By.XPATH, ".//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    count_ingridient = (By.XPATH, ".//div[@class='counter_counter__ZNLkj counter_default__28sqi']")
    order = (By.XPATH, ".//button[text()='Оформить заказ']")
    log_in = (By.XPATH, ".//button[text()='Войти в аккаунт']")


class Detail:
    parent_window = (By.XPATH, ".//h2[text()='Детали ингредиента']/ancestor::div/ancestor::div/ancestor::section")
    open = "opened"
    window = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']")
    heading = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/h2[text()='Детали ингредиента']")
    heading_in_window = (By.XPATH, ".//h2")
    description_in_window = (By.XPATH, ".//p")
    description = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/p[@class='text text_type_main-medium mb-8']")
    button = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']/following-sibling::button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    name_text = "Детали ингредиента"


class Confirm:
    window = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")
    number = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    exit = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")


class Ingridient:
    bread_first = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")
    souce_first = (By.XPATH, ".//p[text()='Соус Spicy-X']/ancestor::a")
    topping_first = (By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']/ancestor::a")
