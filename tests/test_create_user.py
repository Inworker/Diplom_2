import allure
import pytest
import requests
import urls


class TestCreateUser:

    @allure.description('Создание уникального пользователя')
    def test_create_unique_user(self, data_new3):
        response_create_user, payload = data_new3
        assert 200 == response_create_user.status_code and response_create_user.json()["user"]["email"] == payload[
            "email"]

    @allure.description('Создание пользователя, который уже зарегистрирован')
    def test_create_duplicate_user(self, data_new3):
        response_create_user, payload = data_new3
        response_duplicate_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=payload)
        assert 403 == response_duplicate_user.status_code and response_duplicate_user.json()[
            "message"] == "User already exists"

    @pytest.mark.parametrize(
        'field',
        [

            "email", "name"
        ]
    )
    @allure.description('Создание пользователя, если не заполнено одно из обязательных полей')
    def test_create_user_with_missing_required_field(self, data_new3, field):
        response_create_user, payload = data_new3
        del payload[field]
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=payload)
        assert 403 == response_create_user.status_code and response_create_user.json()[
            "message"] == "Email, password and name are required fields"
