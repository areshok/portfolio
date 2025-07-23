from selenium.webdriver.common.by import By


class PageOneLocator:
    first_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    station = (By.XPATH, ".//div[text()='{}']/ancestor::button")
    phone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    button = (By.XPATH, ".//button[text()='Далее']")
    error_fname = (By.XPATH, ".//div[text()='Введите корректное имя']")
    error_lname = (By.XPATH, ".//div[text()='Введите корректную фамилию']")
    error_address = (By.XPATH, ".//div[text()='Введите корректный адрес']")
    error_phone = (By.XPATH, ".//div[text()='Введите корректный номер']")
    error_fname_text = "Введите корректное имя"
    error_lname_text = "Введите корректную фамилию"
    error_address_text = "Введите корректный адрес"
    error_phone_text = "Введите корректный номер"


class PageTwoLocator:
    date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, ".//div[@class='react-datepicker']")
    rent = (By.XPATH, ".//div[text()='* Срок аренды']")
    days = (By.XPATH, ".//div[@class='Dropdown-option']")
    day = (By.XPATH, ".//div[text()='{}']")
    checkbox = (By.XPATH, ".//div[text()='Цвет самоката']/following-sibling::label[text()='{}']")
    comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    order = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    back = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Назад']")


class PageConfirmLocator:
    yes = (By.XPATH, ".//button[text()='Да']")
    no = (By.XPATH, ".//button[text()='Нет']")
    status = (By.XPATH, ".//button[text()='Посмотреть статус']")
    order = (By.XPATH, ".//div[starts-with(text(), 'Номер заказа')]")
    text = "Номер заказа:"
