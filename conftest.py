import pytest
from faker import Faker
from methods.user_methods import UserMethods
from helper import generate_user_data

fake = Faker()
user_methods = UserMethods()


@pytest.fixture
def create_and_delete_user():
    payload = generate_user_data()
    created_response = user_methods.create_user(payload)
    if created_response.status_code == 200:
        access_token = created_response.json()['accessToken']
        yield {
            'response': created_response,
            'payload': payload,
            'access_token': access_token
        }
        user_methods.delete_user(access_token)
    else:
        yield {
            'response': created_response,
            'payload': payload
        }
