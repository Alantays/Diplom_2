import allure
import requests
from urls import BASE_URL, REG_USER_ENDPOINT, LOGIN_USER_ENDPOINT, GET_USER_ENDPOINT


class UserMethods:

    @allure.step("Создание пользователя")
    def create_user(self, payload):
        response = requests.post(f'{BASE_URL}{REG_USER_ENDPOINT}', json=payload)
        return response

    @allure.step("Авторизация пользователя")
    def login_user(self, payload):
        response = requests.post(f'{BASE_URL}{LOGIN_USER_ENDPOINT}', json=payload)
        return response

    @allure.step("Получение информации о пользователе")
    def get_user_info(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.get(f'{BASE_URL}{REG_USER_ENDPOINT}', headers=headers)
        return response

    @allure.step("Изменение данных пользователя")
    def update_user(self, payload, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.patch(f'{BASE_URL}{GET_USER_ENDPOINT}', json=payload, headers=headers)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, access_token):
        headers = {
            'Authorization': access_token
        }
        response = requests.delete(f'{BASE_URL}{GET_USER_ENDPOINT}', headers=headers)
        return response
