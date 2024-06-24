import allure
import requests
import urls
class TestLoginUser:

    @allure.description('Логин под существующим пользователем')
    def test_login_existing_user(self, data_new):
        #Создал пользователя
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        #Удалил имя пользователя из data_new
        del data_new["name"]
        #Сделал запрос авторизации
        responce_login_user = requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL, data = data_new)
        assert 200 == responce_login_user.status_code and responce_login_user.json()["user"]["email"] == data_new["email"]
        token = responce_create_user.json()["accessToken"]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})

    @allure.description('Логин с неверным логином и паролем')
    def test_login_with_invalid_credentials(self):
        responce_login_user = requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL)
        assert 401 == responce_login_user.status_code and responce_login_user.json()["message"] == "email or password are incorrect"