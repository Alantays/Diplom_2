import allure
from methods.order_methods import OrderMethods
from data import UNAUTHORIZED_RESPONSE

order_methods = OrderMethods()


class TestGetOrder:

    @allure.title("Получение заказов пользователя с авторизацией")
    def test_get_user_order_with_authorization(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        response = order_methods.get_orders(access_token)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Получение заказов пользователя без авторизации")
    def test_get_user_order_without_authorization(self):
        response = order_methods.get_orders('')
        assert response.status_code == 401 and response.json() == UNAUTHORIZED_RESPONSE
