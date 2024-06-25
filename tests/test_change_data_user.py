import allure
import requests
import urls
import conftest
import helper
class TestChangeData:

    @allure.description('Изменение данных пользователя с авторизицией')
    def test_authenticated_access(self, data_new):
        # Создал пользователя
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        token = responce_create_user.json()["accessToken"]
        # Удалил имя пользователя из data_new
        del data_new["name"]
        #Сделал еще набор фейковых данных
        change_data_user = helper.CreateCurrierData.generate_fake_user_data()
            # Сделал запрос авторизации
        requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL, data=data_new)

        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL, headers = {"Authorization": token}, data= change_data_user)

        assert 200 == response_data_user.status_code and response_data_user.json()["user"]["email"] == change_data_user["email"]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Authorization": token})

    @allure.description('Изменение данных пользователя без авторизиции')
    def test_unauthenticated_access(self, data_new):
        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL,  data= data_new)
        assert 401 == response_data_user.status_code and response_data_user.json()["message"] == "You should be authorised"



