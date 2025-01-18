import json
from http.client import responses
import httpx
import pytest
from jsonschema import validate
from Core.contracts import REGISTERED_USER_SCHEME
import allure


JSON_FILE = open('Core/new_users_data.json')
USERS_DATA = json.load(JSON_FILE)
BASE_URL = "https://reqres.in/"
REGISTER_USER_URL = "api/register"
UNSUCCESSFUL_REGISTER_BODY = {
    "email": "sydney@fife"
}
LOGIN_USER_URL = "api/login"



@allure.suite('Проверка регистрации пользователя в системе')
@allure.title(f'Проверяем успешную регистрацию пользователя в системе')
@pytest.mark.parametrize('users_data', USERS_DATA)
def test_successful_register(users_data):
    response = httpx.post(BASE_URL + REGISTER_USER_URL, json=users_data)
    with allure.step(f'Делаем запрос по адресу {BASE_URL + REGISTER_USER_URL} и проверяем, что код ответа равен 200'):
        assert response.status_code == 200
    validate(response.json(), REGISTERED_USER_SCHEME)




    # Homework tests
@allure.suite('Проверка регистрации пользователя в системе')
@allure.title(f'Проверяем неуспешную регистрацию пользователя в системе')
def test_unsuccessful_register():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + REGISTER_USER_URL} и проверяем, что код ответа равен 404'):
        response = httpx.post(BASE_URL + REGISTER_USER_URL, json= UNSUCCESSFUL_REGISTER_BODY)
        assert response.status_code == 400
    response_json = response.json()
    validate(response_json, UNSUCCESSFUL_REGISTER_BODY)
    with allure.step('Проверяем, что в теле ответа вернется текст ошибки - "Missing password"'):
        assert response_json['error'] == 'Missing password'



@allure.suite('Проверка входа пользователя в систему')
@allure.title(f'Проверяем успешный вход пользователя в систему')
@pytest.mark.parametrize('users_data', USERS_DATA)
def test_successful_login(users_data):
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LOGIN_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.post(BASE_URL + LOGIN_USER_URL, json=users_data)
        assert response.status_code == 200
    registered_response = httpx.post(BASE_URL + REGISTER_USER_URL, json=users_data)
    get_token = registered_response.json()['token']
    data = response.json()
    with allure.step(f'Проверяем, что токен в ответе соответствует токену, полученному при регистрации'):
             assert data['token'] == get_token
