import httpx
from jsonschema import validate
from Core.contracts import USER_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
NOT_FOUND_USER = "api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение данных пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверяем элемент из списка'):
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
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 200
    data = response.json()['data']

    with allure.step('Проверяем окончание почты'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем, что окончание ссылки на аватар состоит из "id" + "-image.jpg"'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем 404 при получении данных пользователя')
def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + NOT_FOUND_USER)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 404