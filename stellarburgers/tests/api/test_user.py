import allure
import pytest

from stellarburgers.api.user import UserRequest


class TestCaseUser:
    "Тест кейс для проверки пользователя"

    @allure.title("тест: создание уникального пользователя")
    def test_create_unique_user(self, user_cls):
        "тест: создание уникального пользователя"
        print(user_cls)
        response = UserRequest().register(data=user_cls)
        assert response["status"] == 200
        assert response['body']["success"] is True
        assert "accessToken" in response['body']
        assert "refreshToken" in response['body']

    @allure.title("тест: создание пользователя который уже зарегистрирован")
    def test_create_dublicate_user(self, user_cls):
        "тест: создание пользователя который уже зарегистрирован"
        response = UserRequest().register(data=user_cls)
        assert response["status"] == 403
        assert response["body"]["success"] is False
        assert response["body"]["message"] == UserRequest.ResponseText.dublicate

    @pytest.mark.parametrize("field", ["email", "password", "name"])
    @allure.title(
        """
        тест: создание пользователя отсутствует поле {field}
        """
    )
    def test_create_user_missing_field(self, user_def, field):
        """
        тест: создание пользователя отсутствует поле email
        тест: создание пользователя отсутствует поле password
        тест: создание пользователя отсутствует поля name
        """
        user_def.pop(field)
        response = UserRequest().register(data=user_def)
        assert response["status"] == 403
        assert response["body"]["success"] is False
        assert response["body"]["message"] == UserRequest.ResponseText.missing_field_register

    @allure.title("тест: проверка входа в систему созданым пользователем")
    def test_user_login_created(self, user_cls):
        "тест: проверка входа в систему созданым пользователем"
        response = UserRequest().login(data=user_cls)
        assert response["status"] == 200
        assert response['body']["success"] is True
        assert "accessToken" in response['body']
        assert "refreshToken" in response['body']

    @pytest.mark.parametrize("field", ["email", "password",])
    @allure.title("тест: проверка входа в систему с нусуществующем {field}")
    def test_user_login_uncorrect_field(self, user_cls, user_def, field):
        """
        тест: проверка входа в систему с несуществующем email
        тест: проверка входа в систему с несуществующем password
        """
        user = user_cls.copy()
        user[field] = user_def[field]
        response = UserRequest().login(data=user)
        assert response["status"] == 401
        assert response["body"]["success"] is False
        assert response["body"]["message"] == UserRequest.ResponseText.uncorrect_field
