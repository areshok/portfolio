import allure

from stellarburgers.locators.user import UserLocator
from stellarburgers.locators.header import Header
from stellarburgers.locators.constructor import Designer
from stellarburgers.pages.user_page import UserPage
from stellarburgers.data.urls import URLS


class TestLogInRedirect:
    "Тест кейс перенаправлений для входа в систему"

    @allure.title(
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку войти на главной странице
        """
    )
    def test_redirect_log_in_on_home_page(self, browser):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку войти на главной странице
        """
        page = UserPage(browser)
        page.open_url(URLS["ui"]["/"])
        current_url = page.current_url()
        assert current_url == URLS["ui"]["/"]
        page.click(Designer.log_in)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]

    @allure.title(
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку личный кабинет
        """
    )
    def test_redirect_log_in_button_personal_account(self, browser):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку личный кабинет
        """
        page = UserPage(browser)
        page.open_url(URLS["ui"]["/"])
        current_url = page.current_url()
        assert current_url == URLS["ui"]["/"]
        page.click(Header.personal_account)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]

    @allure.title(
        """
        тест: проверка редиректа на страницу входа,
        после нажанития на кнопку в форме регистрации
        """
    )
    def test_redirect_log_in_button_registration_form(self, browser):
        """
        тест: проверка редиректа на страницу входа,
        после нажанития на кнопку в форме регистрации
        """
        page = UserPage(browser)
        page.open_url(URLS["ui"]["register"])
        page.click(UserLocator.RegistrationPage.enter)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]

    @allure.title(
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку на странице восстановление пароля
        """
    )
    def test_redirect_log_in_on_buttom_password_fogot(self, browser):
        """
        тест: проверка редиректа на страницу входа,
        после нажатия на кнопку на странице восстановление пароля
        """
        page = UserPage(browser)
        page.open_url(URLS["ui"]["fogot-password"])
        page.click(UserLocator.RecoveryPasswordPage.enter)
        page.get_element(UserLocator.LoginPage.recover_password)
        current_url = page.current_url()
        assert current_url == URLS["ui"]["login"]
