import allure

from stellarburgers.api.order import OrderReauest
from stellarburgers.api.user import UserRequest


class TestCaseOrder:

    @allure.title("тест: создание заказа авторизированным пользователем")
    def test_create_order_login_user(self, user_def):
        "тест: создание заказа авторизированным пользователем"
        user = UserRequest()
        user.register(data=user_def)
        headers = {"Authorization": user.token}
        order = OrderReauest()
        ingridients = order.get_random_ingridients()
        response = order.create(data=ingridients, headers=headers)
        assert response["status"] == 200
        assert response["body"]["success"] is True
        assert "order" in response["body"]
        assert "name" in response["body"]

    @allure.title(
        """
        тест: создание заказа не авторизированным пользователем
        тест: создание заказа с ингредиентами
        """
    )
    def test_create_order_anonim_user(self):
        """
        тест: создание заказа не авторизированным пользователем
        тест: создание заказа с ингредиентами
        """
        order = OrderReauest()
        ingridients = order.get_random_ingridients()
        response = order.create(data=ingridients)
        assert response["status"] == 200
        assert "name" in response["body"]
        assert "number" in response["body"]["order"]
        assert response['body']["success"] is True

    @allure.title("тест: создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        "тест: создание заказа без ингредиентов"
        response = OrderReauest().create()
        assert response["status"] == 400
        assert response["body"]["success"] is False
        assert response["body"]["message"] == OrderReauest.ResposeText.empty_ingridients

    @allure.title("тест: создание заказа с неправильным хешем ингредиентов")
    def test_create_order_with_an_incorrect_hash_of_ingredients(
        self, uncorrect_hash_ingridient
    ):
        "тест: создание заказа с неправильным хешем ингредиентов"
        response = OrderReauest().create(data=uncorrect_hash_ingridient)
        assert response["status"] == 500
