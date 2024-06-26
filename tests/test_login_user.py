import allure
import requests
import helper
import urls


class TestLoginUser:

    @allure.description('Логин под существующим пользователем')
    def test_login_existing_user(self, data_new3):
        response_create_user, payload = data_new3
        response_login_user = requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL, data=payload)
        assert 200 == response_login_user.status_code and response_login_user.json()["user"]["email"] == payload[
            "email"]

    @allure.description('Логин с неверным логином и паролем')
    def test_login_with_invalid_credentials(self):
        payload = helper.CreateCurrierData.generate_currier_data()
        response_login_user = requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL, data=payload)
        assert 401 == response_login_user.status_code and response_login_user.json()[
            "message"] == "email or password are incorrect"
