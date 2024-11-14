import pytest
import requests
from selenium import webdriver
from helpers import generated_data_user
from data import Url
from data import API


def _get_driver(name):
    if name == 'chrome':
        return webdriver.Chrome()
    elif name == 'firefox':
        return webdriver.Firefox()
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    driver = _get_driver(request.param)
    driver.get(Url.URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_user():
    payload = generated_data_user()
    answer = requests.post(API.CREATE_USER, data=payload)
    token = answer.json().get("accessToken")
    yield payload, answer
    requests.delete(API.DELETE_USER, headers={"Authorization": f'{token}'})
