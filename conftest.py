import pytest
from selenium import webdriver
from helpers.urls import Urls
from helpers.user_helpers import UserRegistration


@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.get(Urls.URL)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    # Регистрируем нового пользователя
    user_data = UserRegistration.register_new_user()
    access_token = user_data['access_token']
    email = user_data['email']
    password = user_data['password']
    payload = user_data['payload']


    yield {
        'access_token': access_token,
        'email': email,
        'password': password,
        'payload': payload
    }

    # Удаляем пользователя после завершения теста
    UserRegistration.delete_user(access_token)
