import httpx
from jsonschema import validate
from Core.contracts import RESOURCE_DATA_SCHEME
import allure

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
SINGLE_NOT_FOUND = "/api/unknown/23"
COLOR_START = "#"
PANTONE_VALUE_MASK = "-"


@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение данных ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверяем код статуса метода'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEME)
            with allure.step('Проверяем, что цвет начинается с "#"'):
                assert item['color'].startswith(COLOR_START)
            with allure.step('Проверяем, что цвет пантона содержит в себе "-"'):
                assert str(PANTONE_VALUE_MASK) in item['pantone_value']
        print(response)


@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение данных одного ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверяем код ответа метода'):
        assert response.status_code == 200
    data = response.json()['data']
    with allure.step('Проверяем, что цвет начинается с "#"'):
        assert data['color'].startswith(COLOR_START)
    assert PANTONE_VALUE_MASK in data['pantone_value']
    print(response)


@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем 404 при получении данных ресурса')
def test_single_resource_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_NOT_FOUND}'):
        response = httpx.get(BASE_URL + SINGLE_NOT_FOUND)
    with allure.step('Проверяем, что метод вернет 404 код'):
        assert response.status_code == 404
    print(response)