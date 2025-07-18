from selenium.webdriver.common.by import By


class UserLocator:

    class AccountPage:
        profile = (By.XPATH, ".//a[text()='Профиль']")
        order_history = (By.XPATH, ".//a[text()='История заказов']")
        exit = (By.XPATH, ".//button[text()='Выход']")
        cancel = (By.XPATH, ".//button[text()='Отмена']")
        save = (By.XPATH, ".//button[text()='Сохранить']")

    class LoginPage:
        email = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
        password = (
            By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
        enter = (By.XPATH, ".//button[text()='Войти']")
        register = (By.XPATH, ".//a[text()='Зарегистрироваться']")
        recover_password = (By.XPATH, ".//a[text()='Восстановить пароль']")

    class RegistrationPage:
        name = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
        email = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
        password = (
            By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
        register = (By.XPATH, ".//button[text()='Зарегистрироваться']")
        enter = (By.XPATH, ".//a[text()='Войти']")
        err_already_there = (
            By.XPATH, ".//p[text()='Такой пользователь уже существует']")
        err_password = (By.XPATH, ".//p[text()='Некорректный пароль']")
        err_password_text = "Некорректный пароль"

    class RecoveryPasswordPage:
        email = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
        recover = (By.XPATH, ".//button[text()='Восстановить']")
        enter = (By.XPATH, ".//a[text()='Войти']")
