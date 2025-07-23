import pytest
import allure

from automated_testing.query.order import OrderRequest
from automated_testing.query.courier import CourierRequest


class TestCaseOrderCreate:

    @pytest.mark.parametrize(
            "color", [
                "BLACK",
                "GREY",
                "BLACK,GREY",
                ""
                ]
    )
    @allure.title("""
    тест: тело ответа содержит track
    тест: можно указать один из цветов — BLACK или GREY
    тест: можно указать оба цвета
    тест: можно совсем не указывать цвет
    """)
    def test_create_order(self, color, get_order_date):
        """
        тест: тело ответа содержит track
        тест: можно указать один из цветов — BLACK или GREY
        тест: можно указать оба цвета
        тест: можно совсем не указывать цвет
        """
        data = get_order_date
        data["color"] = color.split(",")
        response = OrderRequest().create(data)
        assert response['status'] == 201
        assert "track" in response["body"]


class TestCaseOrderList:

    @allure.title("тест: проверка тела списка заказов")
    def test_list_order_body_content(self):
        "тест: проверка тела списка заказов"
        response = OrderRequest().list()
        # проверка наличия ключей в теле ответа
        assert list(response["body"]) == ['orders', 'pageInfo', 'availableStations']
        # проверка наличия ключей в заказе
        assert "id" in response["body"]["orders"][0]
        assert "courierId" in response["body"]["orders"][0]
        assert "firstName" in response["body"]["orders"][0]
        assert "lastName" in response["body"]["orders"][0]
        assert "address" in response["body"]["orders"][0]
        assert "metroStation" in response["body"]["orders"][0]
        assert "phone" in response["body"]["orders"][0]
        assert "rentTime" in response["body"]["orders"][0]
        assert "deliveryDate" in response["body"]["orders"][0]
        assert "track" in response["body"]["orders"][0]
        assert "comment" in response["body"]["orders"][0]
        assert "createdAt" in response["body"]["orders"][0]
        assert "updatedAt" in response["body"]["orders"][0]
        assert "updatedAt" in response["body"]["orders"][0]
        assert "status" in response["body"]["orders"][0]
        # првоерка наличия ключей в pageInfo
        assert "page" in response["body"]["pageInfo"]
        assert "total" in response["body"]["pageInfo"]
        assert "limit" in response["body"]["pageInfo"]
        # првоерка наличия ключей в availableStations
        assert "name" in response["body"]["availableStations"][0]
        assert "number" in response["body"]["availableStations"][0]
        assert "color" in response["body"]["availableStations"][0]


class TestCaseAcceptOrder:

    def test_correct_query_accept_order(self, get_order_date, get_user_data):
        """
        тест: успешный запрос возвращает{"ok":true}
        """
        query = OrderRequest()
        response = query.create(get_order_date)
        track = response["body"]["track"]
        id_order = query.get_order(track)["body"]["order"]["id"]
        courier = CourierRequest()
        courier.register(**get_user_data)
        del get_user_data["firstname"]
        id_courier = courier.login(**get_user_data)["body"]["id"]
        response = query.accept_order(id_order, id_courier)
        assert response["status"] == 200
        assert response["body"]["ok"] is True

    @allure.title("тест: появление ошибки, id курьера отсутсвует")
    def test_query_accept_order_missing_id_courier(self, get_order_date):
        "тест: появление ошибки, id курьера отсутсвует"
        query = OrderRequest()
        response = query.create(get_order_date)
        track = response["body"]["track"]
        id_order = query.get_order(track)["body"]["order"]["id"]
        response = query.accept_order(id_order, '')
        assert response["status"] == 400
        assert response["body"][query.ResponseField.err] == query.ResponseText.accept_order_missing

    @allure.title("тест: если передать неверный id курьера, запрос вернёт ошибку")
    def test_query_accept_order_uncorrect_id_courier(self, get_order_date):
        "тест: если передать неверный id курьера, запрос вернёт ошибку"
        query = OrderRequest()
        response = query.create(get_order_date)
        track = response["body"]["track"]
        id_order = query.get_order(track)["body"]["order"]["id"]
        response = query.accept_order(id_order, 99999999)
        assert response["status"] == 400
        assert response["body"][query.ResponseField.err] == query.ResponseText.courier_non_exist

    @allure.title("тест: если не передать id заказа, запрос вернёт ошибку")
    def test_query_accept_order_missing_id_order(self, get_user_data):
        "тест: если не передать id заказа, запрос вернёт ошибку"
        query = OrderRequest()
        courier = CourierRequest()
        courier.register(**get_user_data)
        del get_user_data["firstname"]
        id_courier = courier.login(**get_user_data)["body"]["id"]
        response = query.accept_order("", id_courier)
        assert response["status"] == 404
        assert response["body"][query.ResponseField.err] == query.ResponseText.order_null

    @allure.title("тест: если передать неверный id заказа, запрос вернёт ошибку.")
    def test_query_accept_order_uncorrect_order_id(self, get_user_data, get_order_date):
        "тест: если передать неверный id заказа, запрос вернёт ошибку."
        query = OrderRequest()
        courier = CourierRequest()
        courier.register(**get_user_data)
        del get_user_data["firstname"]
        id_courier = courier.login(**get_user_data)["body"]["id"]
        response = query.accept_order(999999999, id_courier)
        assert response["status"] == 404
        assert response["body"][query.ResponseField.err] == query.ResponseText.order_non_exists


class TestCaseGetOrder:

    @allure.title("тест: успешный запрос возвращает объект с заказом")
    def test_correct_query_get_order(self, get_order_date):
        "тест: успешный запрос возвращает объект с заказом"
        query = OrderRequest()
        track = query.create(get_order_date)["body"]["track"]
        response = query.get_order(track)
        assert response["status"] == 200
        assert query.ResponseField.get in response["body"]

    @allure.title("тест: запрос без номера заказа возвращает ошибку")
    def test_query_get_order_missing_track(self):
        "тест: запрос без номера заказа возвращает ошибку"
        response = OrderRequest().get_order('')
        assert response["status"] == 400
        assert response["body"][OrderRequest.ResponseField.err] == OrderRequest.ResponseText.order_null

    @allure.title("тест: запрос с несуществующим заказом возвращает ошибку")
    def test_query_get_order_non_exists_track(self):
        "тест: запрос с несуществующим заказом возвращает ошибку"
        response = OrderRequest().get_order(999999999)
        assert response["status"] == 404
        assert response["body"][OrderRequest.ResponseField.err] == OrderRequest.ResponseText.non_exists_track
