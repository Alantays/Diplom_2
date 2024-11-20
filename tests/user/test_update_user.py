import allure
from methods.user_methods import UserMethods
from helper import generate_new_email
from data import UNAUTHORIZED_RESPONSE

user_methods = UserMethods()


class TestUpdateUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_modify_user_with_authorization(self, create_and_delete_user):
        access_token = create_and_delete_user['access_token']
        updated_payload = generate_new_email()
        update_response = user_methods.update_user(updated_payload, access_token)
        assert update_response.status_code == 200 and update_response.json()["success"] is True

    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_without_authorization(self):
        updated_payload = generate_new_email()
        update_response = user_methods.update_user(updated_payload, '')
        assert update_response.status_code == 401 and update_response.json() == UNAUTHORIZED_RESPONSE
