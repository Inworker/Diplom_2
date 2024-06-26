import pytest
import requests
import helper
import urls


@pytest.fixture(scope='function')
def data_new3():
    payload = helper.CreateCurrierData().generate_currier_data()
    response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=payload)
    yield response_create_user, payload
    token = response_create_user.json()["accessToken"]
    requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=payload, headers={"Authorization": token})
