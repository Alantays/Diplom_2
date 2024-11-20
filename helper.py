from faker import Faker
import random
from methods.order_methods import OrderMethods

fake = Faker()


def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }


def generate_user_data_missing_field():
    return {
        "email": fake.email(),
        "name": fake.name()
    }


def get_login_payload(payload):
    return {
        "email": payload["email"],
        "password": payload["password"]
    }


def generate_wrong_creds():
    return {
        "email": fake.email(),
        "password": fake.password()
    }


def generate_new_email():
    return {
        "email": fake.email()
    }


def generate_ingredients():
    order_methods = OrderMethods()
    ingredients_data = order_methods.get_ingredients()

    buns = []
    mains = []

    for item in ingredients_data['data']:
        if item['type'] == 'bun':
            buns.append(item['_id'])
        elif item['type'] == 'main':
            mains.append(item['_id'])

    random_bun = random.choice(buns)
    random_main = random.choice(mains)

    return [random_bun, random_main]
