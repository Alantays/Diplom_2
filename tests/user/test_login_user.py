import allure
from methods.user_methods import UserMethods
from data import LOGIN_ERROR_RESPONSE
from helper import get_login_payload, generate_wrong_creds

user_methods = UserMethods()


class TestLoginUser:
    @allure.title("Авторизация с валидными учетными данными")
    def test_login_with_existing_credentials(self, create_and_delete_user):
        payload = create_and_delete_user['payload']
        login_payload = get_login_payload(payload)
        login_response = user_methods.login_user(login_payload)
        assert login_response.status_code == 200 and login_response.json()["success"] is True

    @allure.title("Авторизация с невалидными учетными данными")
    def test_login_with_non_existing_credentials(self, create_and_delete_user):
        payload = generate_wrong_creds()
        login_response = user_methods.login_user(payload)
        assert login_response.status_code == 401 and login_response.json() == LOGIN_ERROR_RESPONSE
