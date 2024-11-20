from methods.order_methods import OrderMethods
import allure
from data import (
    VALID_INGREDIENTS_PAYLOAD,
    EMPTY_INGREDIENTS_PAYLOAD,
    INVALID_INGREDIENTS_PAYLOAD,
    EMPTY_INGREDIENTS_RESPONSE,
    INVALID_INGREDIENTS_RESPONSE
)

order_methods = OrderMethods()


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_authorization_and_ingredients(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(VALID_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        response = order_methods.create_order(VALID_INGREDIENTS_PAYLOAD, '')
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(EMPTY_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 400 and response.json() == EMPTY_INGREDIENTS_RESPONSE

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.create_order(INVALID_INGREDIENTS_PAYLOAD, access_token)
        assert response.status_code == 400 and response.json() == INVALID_INGREDIENTS_RESPONSE
