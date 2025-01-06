import httpx
from jsonschema import validate
from ApiTests.Core.contracts import RESOURCE_DATA_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
SINGLE_NOT_FOUND = "/api/unknown/23"
COLOR_START = "#"
PANTONE_VALUE_MASK = "-"



def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEME)
        assert item['color'].startswith(COLOR_START)
        assert str(PANTONE_VALUE_MASK) in item['pantone_value']
        print(response)

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith(COLOR_START)
    assert PANTONE_VALUE_MASK in data['pantone_value']
    print(response)

def test_single_resource_not_found():
    response = httpx.get(BASE_URL + SINGLE_NOT_FOUND)
    assert response.status_code == 404
    print(response)