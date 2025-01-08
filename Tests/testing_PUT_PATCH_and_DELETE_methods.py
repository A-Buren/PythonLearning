from dataclasses import replace
from http.client import responses

import httpx
from jsonschema import validate
import datetime
from Core.contracts import PUT_AND_PATCH_UPDATED_USER_SCHEME
import allure


BASE_URL = "https://reqres.in/"
UPDATE_AND_DELETE_USER = "api/users/2"
DATE_FORMAT = "T"
BODY = {
        "name": "morpheus",
        "job": "zion resident"
    }


@allure.suite('Проверка PUT, PATCH и DELETE методов 123')
@allure.title('Проверяем обновление пользователя PUT методом')
def test_update_user_put_method():
    body = BODY
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_AND_DELETE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_AND_DELETE_USER, json=body)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 200
    response_json = response.json()
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, PUT_AND_PATCH_UPDATED_USER_SCHEME)
    with allure.step('Проверяем, что "job" в ответе соответствует запросу'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что "name" в ответе соответствует запросу'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert updated_date[0:16] == current_date[0:16]
    with allure.step('Проверяем окончание у "updatedAt" (в т.ч. проверяем формат Z)'):
        assert updated_date.endswith('Z')
    with allure.step('Проверяем формат "updatedAt"'):
        assert DATE_FORMAT in response_json['updatedAt']


@allure.suite('Проверка PUT, PATCH и DELETE методов 123')
@allure.title('Проверяем обновление пользователя PATCH методом')
def test_update_user_patch_method():
    body = BODY
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_AND_DELETE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_AND_DELETE_USER, json=body)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 200
    response_json = response.json()
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, PUT_AND_PATCH_UPDATED_USER_SCHEME)
    with allure.step('Проверяем, что "job" в ответе соответствует запросу'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что "name" в ответе соответствует запросу'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert updated_date[0:16] == current_date[0:16]
    with allure.step('Проверяем окончание у "updatedAt" (в т.ч. проверяем формат Z)'):
        assert updated_date.endswith('Z')
    with allure.step('Проверяем формат "updatedAt"'):
        assert DATE_FORMAT in response_json['updatedAt']


@allure.suite('Проверка PUT, PATCH и DELETE методов 123')
@allure.title('Проверяем удаление пользователя DELETE методом')
def test_delete_user():
    with allure.step('Вызываем метод'):
        response = httpx.delete(BASE_URL + UPDATE_AND_DELETE_USER)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 204
