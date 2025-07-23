import pytest
import allure

from automated_testing.query.courier import CourierRequest
from automated_testing.data.settings import CREATED_COURIER


class TestCaseCreateCoruier:


    def _test_register_unique_corier(self, get_user_data):
        """
        тест: курьера можно создать
        тест: успешный запрос возвращает {"ok":true}
        тест: запрос возвращает правильный код ответа
        """
        response = CourierRequest().register(**get_user_data)
        assert response["status"] == 201
        assert response["body"][CourierRequest.ResponseField.create] is True

    def _test_cant_create_two_identical_couriers(self, get_user_data):
        """
        тест: нельзя создать двух одинаковых курьеров
        тест:если создать пользователя с логином, который уже есть,
        возвращается ошибка.
        """
        response = CourierRequest().register(**get_user_data)
        assert response["status"] == 201
        assert response["body"][CourierRequest.ResponseField.create] is True
        response = CourierRequest().register(**get_user_data)
        assert response["status"] == 409
        assert CourierRequest.ResponseText.dublicat_user in response["body"][CourierRequest.ResponseField.err]

    def _test_create_courier_required_fields_filled(self,get_user_data):
        "тест: чтобы создать курьера, нужно передать в ручку все обязательные поля"
        del get_user_data["firstname"]
        response = CourierRequest().register(**get_user_data)
        assert response["status"] == 201
        assert response["body"][CourierRequest.ResponseField.create] is True

    @pytest.mark.parametrize("field", ["login", "password"])
    def _test_create_courier_missing_field(self, field, get_user_data):
        "тест: если одного из полей нет, запрос возвращает ошибку"
        del get_user_data[field]
        response = CourierRequest().register(**get_user_data)
        assert response["status"] == 400
        assert response["body"][CourierRequest.ResponseField.err] == CourierRequest.ResponseText.missing_field_register


class TestCaseLoginCourier:

    @allure.title(
        """
        тест: курьер может авторизоваться
        тест: успешный запрос возвращает id
        тест: для авторизации нужно передать все обязательные поля
        """
    )
    def test_login_corier_correct_data(self, courier):
        """
        тест: курьер может авторизоваться
        тест: успешный запрос возвращает id
        тест: для авторизации нужно передать все обязательные поля
        """
        response = CourierRequest().login(**courier)
        assert response["status"] == 200
        assert CourierRequest.ResponseField.login in response["body"]

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("тест: система вернёт ошибку, если неправильно указать логин или пароль")
    def test_login_courier_uncorrect_data_field(self, field, courier):
        "тест: система вернёт ошибку, если неправильно указать логин или пароль"
        courier[field] = "new_value"
        response = CourierRequest().login(**courier)
        assert response["status"] == 404
        assert CourierRequest.ResponseText.non_existent == response["body"][CourierRequest.ResponseField.err]

    @pytest.mark.skip(
        """
        сервер не дает ответа даже в postman,
        запрос просто долго обрабатывается,
        тест отключен
        """
    )
    @allure.title("тест: если password поля нет, запрос возвращает ошибку")
    def test_login_courier_missing_field_login(self):
        "тест: если password поля нет, запрос возвращает ошибку"
        data = {"login": CREATED_COURIER["login"]}
        response = CourierRequest().login(**data)
        assert response["status"] == 400
        assert CourierRequest.ResponseText.missing_field_login == response["body"][CourierRequest.ResponseField.err]

    @allure.title("тест: если login поля нет, запрос возвращает ошибку")
    def test_login_courier_missing_field_password(self):
        """
        тест: если login поля нет, запрос возвращает ошибку
        """
        data = {"password": CREATED_COURIER["password"]}
        response = CourierRequest().login(**data)
        assert response["status"] == 400
        assert CourierRequest.ResponseText.missing_field_login == response["body"][CourierRequest.ResponseField.err]

    @allure.title("тест: авторизация под несуществующем курьером, возращается ошибка")
    def test_login_courier_not_existing(self, get_user_data):
        "тест: авторизация под несуществующем курьером, возращается ошибка"
        del get_user_data["firstname"]
        response = CourierRequest().login(**get_user_data)
        assert response["status"] == 404
        assert response["body"][CourierRequest.ResponseField.err] == CourierRequest.ResponseText.non_existent


class TestCaseCourierDelete:

    @allure.title(" тест: успешный запрос возвращает 'ok':'true'")
    def test_correct_data_delete_courier(self, get_user_data):
        """
        тест: успешный запрос возвращает{"ok":true}
        """
        query = CourierRequest()
        response = query.register(**get_user_data)
        del get_user_data["firstname"]
        response = query.login(**get_user_data)
        id = response["body"]["id"]
        response = query.delete_courier(id)
        assert response["status"] == 200
        assert response["body"]["ok"] is True

    @allure.title("тест: если отправить запрос без id, вернётся ошибка")
    @allure.description("Должен возвзращать код 400, но возвращает 404")
    def test_getting_an_error_missing_id(self):
        "тест: если отправить запрос без id, вернётся ошибка"
        response = CourierRequest().delete_courier(id_courier="")
        assert response["status"] == 400
        assert response["body"][CourierRequest.ResponseField.err] == CourierRequest.ResponseText.missing_id_delete

    @allure.title("тест: если отправить запрос с несуществующим id, вернётся ошибка")
    def test_getting_an_error_id_courier_non_exists(self):
        "тест: если отправить запрос с несуществующим id, вернётся ошибка"
        response = CourierRequest().delete_courier(id_courier=99999999)
        assert response["status"] == 404
        assert response["body"][CourierRequest.ResponseField.err] == CourierRequest.ResponseText.non_existent_delete
