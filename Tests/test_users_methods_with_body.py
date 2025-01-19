import httpx
from jsonschema import validate
from Core.contracts import CREATED_USER_SCHEME
from Core.contracts import UPDATED_USER_SCHEME
import datetime
import allure


BASE_URL = "https://reqres.in/"
CREATE_USER_URL = "api/users"
SECONDARY_USER_URL = "api/users/2"
DATE_FORMAT = "T"
BODY = {
        "name": "morpheus",
        "job": "zion resident"
    }

@allure.suite('Проверка POST метода на создание пользователя')
@allure.title('Проверка создания пользователя c указанием "Name" и "Job" в теле запроса')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.post(BASE_URL + CREATE_USER_URL, json=body)
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, CREATED_USER_SCHEME)

    with allure.step('Проверяем, что "name" в ответе соответствует "name", переданному в теле запроса'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что "job" в ответе соответствует "job", переданному в теле запроса'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка POST метода на создание пользователя')
@allure.title('Проверка создания пользователя без указания "Name" в теле запроса')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.post(BASE_URL + CREATE_USER_URL, json=body)
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, CREATED_USER_SCHEME)

    with allure.step('Проверяем, что "job" в ответе соответствует "job", переданному в теле запроса'):
        assert response_json['job'] == body['job']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка POST метода на создание пользователя')
@allure.title('Проверка создания пользователя без указания "Job" в теле запроса')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.post(BASE_URL + CREATE_USER_URL, json=body)
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, CREATED_USER_SCHEME)

    with allure.step('Проверяем, что "name" в ответе соответствует "name", переданному в теле запроса'):
        assert response_json['name'] == body['name']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert creation_date[0:16] == current_date[0:16]




    # Homework tests
@allure.suite('Проверка PUT, PATCH и DELETE методов')       #123 писал для отладки, забыл удалить
@allure.title('Проверяем обновление пользователя PUT методом')
def test_update_user_put_method():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SECONDARY_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.put(BASE_URL + SECONDARY_USER_URL, json=BODY)
        assert response.status_code == 200

    response_json = response.json()
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())              # Не понимаю, почему "utcnow" автоматически зачеркивается
    validate(response_json, UPDATED_USER_SCHEME)

    with allure.step('Проверяем, что "job" в ответе соответствует "job", переданному в теле запроса'):
        assert response_json['job'] == BODY['job']
    with allure.step('Проверяем, что "name" в ответе соответствует "name", переданному в теле запроса'):
        assert response_json['name'] == BODY['name']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert updated_date[0:16] == current_date[0:16]
    with allure.step('Проверяем окончание у "updatedAt" (в т.ч. проверяем формат Z)'):
        assert updated_date.endswith('Z')
    with allure.step('Проверяем формат "updatedAt"'):
        assert DATE_FORMAT in response_json['updatedAt']


@allure.suite('Проверка PUT, PATCH и DELETE методов')
@allure.title('Проверяем обновление пользователя PATCH методом')
def test_update_user_patch_method():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SECONDARY_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.patch(BASE_URL + SECONDARY_USER_URL, json=BODY)
        assert response.status_code == 200
    response_json = response.json()
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())              # Не понимаю, почему "utcnow" автоматически зачеркивается
    validate(response_json, UPDATED_USER_SCHEME)
    with allure.step('Проверяем, что "job" в ответе соответствует "job", переданному в теле запроса'):
        assert response_json['job'] == BODY['job']
    with allure.step('Проверяем, что "name" в ответе соответствует "name", переданному в теле запроса'):
        assert response_json['name'] == BODY['name']
    with allure.step('Проверяем, что "updatedAt" соответствует дате и времени вызова метода'):
        assert updated_date[0:16] == current_date[0:16]
    with allure.step('Проверяем окончание у "updatedAt" (в т.ч. проверяем формат Z)'):
        assert updated_date.endswith('Z')
    with allure.step('Проверяем формат "updatedAt"'):
        assert DATE_FORMAT in response_json['updatedAt']


@allure.suite('Проверка PUT, PATCH и DELETE методов')
@allure.title('Проверяем удаление пользователя DELETE методом')
def test_delete_user():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SECONDARY_USER_URL} и проверяем, что код ответа равен 200'):
        response = httpx.delete(BASE_URL + SECONDARY_USER_URL)
        assert response.status_code == 204