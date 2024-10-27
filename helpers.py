import random
import string
import requests
from data import Ingredients, API


def generated_data_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = generate_random_string(10)
    email = generate_random_string(10) + '@yandex.ru'
    password = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


def create_order(resp):
    token = resp.json().get("accessToken")
    ingredients = {"ingredients": [Ingredients.FLUOR_BUN, Ingredients.BIO_CUTLET, Ingredients.SAUCE_SPICY]}
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    response = requests.post(API.CREATE_ORDER, headers=headers, json=ingredients)
    return response
