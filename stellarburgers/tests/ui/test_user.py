import allure


from stellarburgers.locators.user import UserLocator
from stellarburgers.locators.header import Header
from stellarburgers.pages.user_page import UserPage
from stellarburgers.data.urls import URLS


class TestCaseUser:
    "Тест кейс для порверки UI пользователя"

    @allure.title("тест: регистрация пользователя с корректными данными")
    def test_registration_user_correct_data(self, browser, user_def):
        "тест: регистрация пользователя с корректными данными"
        page = UserPage(browser)
        page.open_url(URLS["ui"]["register"])
        page.registration(user_def)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]

    def test_registration_user_error_uncorrect_password(
            self, browser, user_def):
        "тест: появление ошибки, длина пароля 5 символов"
        page = UserPage(browser)
        page.open_url(URLS["ui"]["register"])
        user_def["password"] = "12345"
        page.registration(user_def)
        error = page.get_element(UserLocator.RegistrationPage.err_password)
        assert error.text == UserLocator.RegistrationPage.err_password_text

    @allure.title("тест: переход в личный кабинет с главной страницы")
    def test_auth_user_transition_to_personal_account(self, auth_browser):
        "тест: переход в личный кабинет с главной страницы"
        page = UserPage(auth_browser)
        page.click(Header.personal_account)
        current_url = page.current_url()
        assert current_url in URLS["ui"]["profile"]

    @allure.title(
        "тест: Переход из личного кабинета на конструктор бургера нажатием"
        " на кнопку конструктор"
    )
    def test_auth_user_transition_personal_account_to_constructor_button(
        self, auth_browser
    ):
        """
        тест: Переход из личного кабинета на конструктор бургера нажатием
        на кнопку конструктор
        """
        page = UserPage(auth_browser)
        page.click(Header.personal_account)
        current_url = page.current_url()
        assert current_url in URLS["ui"]["profile"]
        page.click(Header.constuctor)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["/"]

    @allure.title(
        "тест: переход из личного кабинета на главную страницу нажанием"
        " на логотип"
    )
    def test_auth_user_transition_personal_account_to_logo_button(
        self, auth_browser
    ):
        """
        тест: переход из личного кабинета на главную страницу нажанием
        на логотип
        """
        page = UserPage(auth_browser)
        page.click(Header.personal_account)
        current_url = page.current_url()
        assert current_url in URLS["ui"]["profile"]
        page.click(Header.logo)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["/"]

    @allure.title("тест: переход из личного кабинета на домашнюю страницу")
    def test_auth_user_ransition_personal_account_main_url(self, auth_browser):
        "тест: переход из личного кабинета на домашнюю страницу"
        page = UserPage(auth_browser)
        page.click(Header.personal_account)
        current_url = page.current_url()
        assert current_url in URLS["ui"]["profile"]
        page.open_url(URLS["ui"]["/"])
        current_url = page.current_url()
        assert current_url == URLS["ui"]["/"]

    @allure.title("тест: выход из учетной записи")
    def test_auth_user_exit_in_account(self, auth_browser):
        "тест: выход из учетной записи"
        page = UserPage(auth_browser)
        page.click(Header.personal_account)
        current_url = page.current_url()
        assert current_url in URLS["ui"]["profile"]
        page.click(UserLocator.AccountPage.exit)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]
