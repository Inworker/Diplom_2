import allure
import requests
import conftest
import api_burger
import data
import helper
import urls



class TestCreateUser:

    @allure.description('Создание уникального пользователя')
    def test_create_unique_user(self, data_new):
        # payload = helper.CreateCurrierData().generate_currier_data()
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        # print(data_new["email"])
        assert 200 == responce_create_user.status_code and responce_create_user.json()["user"]["email"] == data_new["email"]
        token = responce_create_user.json()["accessToken"]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})

    @allure.description('Создание пользователя, который уже зарегистрирован')
    def test_create_duplicate_user(self, data_new):
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        responce_duplicate_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        print(responce_duplicate_user.text)
        assert 403 == responce_duplicate_user.status_code and responce_duplicate_user.json()["message"] == "User already exists"
        token = response_create_user.json()["accessToken"]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})



    @allure.description('Создание пользователя, если не заполнено одно из обязательных полей')
    def test_create_user_with_missing_required_field(self):
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL)
        assert 403 == response_create_user.status_code and response_create_user.json()["message"] == "Email, password and name are required fields"
