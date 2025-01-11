import httpx
from jsonschema import validate
from Core.contracts import USER_DATA_SCHEME
from Core.contracts import RESOURCE_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS_URL = "api/users?page=2"
SINGLE_USER_URL = "api/users/2"
NOT_FOUND_USER_URL = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"
LIST_RESOURCE_URL = "api/unknown"
SINGLE_RESOURCE_URL = "api/unknown/2"
SINGLE_NOT_FOUND_URL = "/api/unknown/23"
COLOR_START = "#"
PANTONE_VALUE_MASK = "-"


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение данных пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS} и проверяем, что код ответа равен 200'):
        response = httpx.get(BASE_URL + LIST_USERS)
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка {item['first_name'] + ' ' + item['last_name']}'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание почты'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверяем наличие "id" в ссылке на аватарку'):
                assert str(item['id']) in item['avatar']
            with allure.step('Проверяем, что аватарка заканчивается на "id" + "-image.jpg"'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение данных одного пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS} и проверяем, что код ответа равен 200'):
        response = httpx.get(BASE_URL + SINGLE_USER)
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем окончание почты'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем, что окончание ссылки на аватар состоит из "id" + "-image.jpg"'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем 404 при получении данных пользователя')
def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS} и проверяем, что код ответа равен 404'):
        response = httpx.get(BASE_URL + NOT_FOUND_USER)
        assert response.status_code == 404



    #Homework tests
@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение данных ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_RESOURCE} и проверяем, что метод вернет 200 код'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка {item['name']}'):
            validate(item, RESOURCE_DATA_SCHEME)
            with allure.step('Проверяем, что цвет начинается с "#"'):
                assert item['color'].startswith(COLOR_START)
            with allure.step('Проверяем, что цвет пантона содержит в себе "-"'):
                assert str(PANTONE_VALUE_MASK) in item['pantone_value']


@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение данных одного ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_RESOURCE} и проверяем, что метод вернет 200 код'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем, что цвет начинается с "#"'):
        assert data['color'].startswith(COLOR_START)
    assert PANTONE_VALUE_MASK in data['pantone_value']


@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем 404 при получении данных ресурса')
def test_single_resource_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_NOT_FOUND} и проверяем, что метод вернет 404 код'):
        response = httpx.get(BASE_URL + SINGLE_NOT_FOUND)
        assert response.status_code == 404
