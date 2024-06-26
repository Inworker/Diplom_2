import allure
import requests

import helper
import urls


class TestGetOrderOfUser:
    @allure.description('Получение списка заказов авторизованного пользователя')
    def test_authenticated_user(self, data_new3):
        response_create_user, payload = data_new3
        token = response_create_user.json()["accessToken"]
        requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token},
                      data=helper.CreateCurrierData.SECOND_INGREDIENT)
        requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token},
                      data=helper.CreateCurrierData.SECOND_INGREDIENT)
        list_of_orders = requests.get(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token})
        assert 200 == list_of_orders.status_code and len(list_of_orders.json()["orders"]) == 2

    @allure.description('Получение списка заказов неавторизованного пользователя')
    def test_unauthenticated_user(self):
        list_of_orders = requests.get(urls.BASE_URL + urls.CREATE_ORDER_URL)
        assert 401 == list_of_orders.status_code and list_of_orders.json()["message"] == "You should be authorised"
