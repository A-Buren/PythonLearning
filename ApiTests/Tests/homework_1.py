from http.client import responses

import httpx
from jsonschema import validate
from ApiTests.Core.contracts import USER_DATA_SCHEME_For_Homework

Base_Url = "https://reqres.in/"
List_Resource = "api/unknown"
Single_Resource = "api/unknown/2"
Single_Not_found = "/api/unknown/23"
Color_start = "#"
Pantone_value_mask = "-"


def test_list_resource():
    response = httpx.get(Base_Url + List_Resource)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME_For_Homework)
        assert item['color'].startswith(Color_start)
        # assert item['pantone_value'].contains(Pantone_value_mask)         #-- не работает
        # assert item['pantone_value'].check(str(Pantone_value_mask))       #-- не работает
        assert str(Pantone_value_mask) in item['pantone_value']
        print(response)

def test_single_resource():
    response = httpx.get(Base_Url + Single_Resource)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith(Color_start)
    assert str(Pantone_value_mask) in data['pantone_value']
    print(response)

def test_single_resource_not_found():
    response = httpx.get(Base_Url + Single_Not_found)
    assert response.status_code == 404
    print(response)