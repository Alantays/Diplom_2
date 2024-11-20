import allure
from methods.user_methods import UserMethods
from data import DUP_USER_RESPONSE, MIS_FIELD_RESPONSE
from helper import generate_user_data_missing_field

user_methods = UserMethods()


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_and_delete_user):
        response = create_and_delete_user['response']
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, create_and_delete_user):
        payload = create_and_delete_user['payload']
        duplicate_response = user_methods.create_user(payload)
        assert duplicate_response.status_code == 403 and duplicate_response.json() == DUP_USER_RESPONSE

    @allure.title("Создание пользователя без указания обязательного поля")
    def test_create_user_with_missing_field(self):
        payload = generate_user_data_missing_field()
        response = user_methods.create_user(payload)
        assert response.status_code == 403 and response.json() == MIS_FIELD_RESPONSE
