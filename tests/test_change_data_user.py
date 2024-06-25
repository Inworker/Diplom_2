import allure
import pytest
import requests
import urls
import conftest
import helper
class TestChangeData:

    @pytest.mark.parametrize(
        'field',
        [
            "email", "name"
        ]
    )
    @allure.description('Изменение данных пользователя с авторизицией')
    def test_authenticated_access(self, data_new, field):
        # Создал пользователя
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        token = responce_create_user.json()["accessToken"]
        # Удалил имя пользователя из data_new
        del data_new["name"]
        #Сделал еще набор фейковых данных
        change_data_user = helper.CreateCurrierData.generate_fake_user_data()

        # Выводим данные для отладки
            # Сделал запрос авторизации
        requests.post(urls.BASE_URL + urls.AUTH_LOGIN_URL, data=data_new)
        # Выводим данные из ответа для отладки
        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL, headers = {"Authorization": token}, data= {field: change_data_user[field]})

        assert 200 == response_data_user.status_code and response_data_user.json()["user"][field] == change_data_user[field]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Authorization": token})

    @pytest.mark.parametrize(
        'field',
        [
            "email", "name"
        ]
    )
    @allure.description('Изменение данных пользователя без авторизиции')
    def test_unauthenticated_access(self, data_new, field):
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        # Сделал еще набор фейковых данных
        change_data_user = helper.CreateCurrierData.generate_fake_user_data()
        response_data_user = requests.patch(urls.BASE_URL + urls.AUTH_USER_URL,
                                            data={field: change_data_user[field]})

        assert 401 == response_data_user.status_code and response_data_user.json()["message"] == "You should be authorised"



