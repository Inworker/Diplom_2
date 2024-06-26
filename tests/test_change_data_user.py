import allure
import pytest
import requests
import urls
import helper


class TestChangeData:

    @pytest.mark.parametrize(
        'field',
        [
            "email", "name"
        ]
    )
    @allure.description('Изменение данных пользователя с авторизицией')
    def test_authenticated_access(self, data_new3, field):
        response_create_user, payload = data_new3
        token = response_create_user.json()["accessToken"]
        change_data_user = helper.CreateCurrierData.generate_fake_user_data()
        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL, headers={"Authorization": token},
                                            data={field: change_data_user[field]})
        assert 200 == response_data_user.status_code and response_data_user.json()["user"][field] == change_data_user[
            field]

    @pytest.mark.parametrize(
        'field',
        [
            "email", "name"
        ]
    )
    @allure.description('Изменение данных пользователя без авторизиции')
    def test_unauthenticated_access(self, data_new3, field):
        change_data_user = helper.CreateCurrierData.generate_fake_user_data()
        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL,
                                            data={field: change_data_user[field]})
        assert 401 == response_data_user.status_code and response_data_user.json()[
            "message"] == "You should be authorised"
