import allure
import requests
from urls import BASE_URL, ORDERS_ENDPOINT, INGREDIENTS_ENDPOINT


class OrderMethods:

    @allure.step("Получение заказов пользователя")
    def get_orders(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.get(f'{BASE_URL}{ORDERS_ENDPOINT}', headers=headers)
        return response

    @allure.step("Создание заказа")
    def create_order(self, payload, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.post(f'{BASE_URL}{ORDERS_ENDPOINT}', json=payload, headers=headers)
        return response

    @allure.step("Получение ингредиентов")
    def get_ingredients(self):
        response = requests.get(f'{BASE_URL}{INGREDIENTS_ENDPOINT}')
        return response.json()
