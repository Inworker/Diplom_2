import allure
import requests
import urls
class TestGetOrderOfUser:
    @allure.description('Получение списка заказов авторизованного пользователя')
    def test_authenticated_user(self, data_new):
        #Создал пользователя
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        #Забрал токен
        token = response_create_user.json()["accessToken"]
        #Создал 2 заказа
        requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token}, data={"ingredients": "61c0c5a71d1f82001bdaaa6f"})
        requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token}, data={"ingredients": "61c0c5a71d1f82001bdaaa6f"})
        list_of_orders = requests.get(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token})
        assert 200 == list_of_orders.status_code and len(list_of_orders.json()["orders"]) == 2


#         # # payload = helper.CreateCurrierData().generate_currier_data()
#         # responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
#         # # print(data_new["email"])
#         # assert 200 == responce_create_user.status_code and responce_create_user.json()["user"]["email"] == data_new["email"]
#         # token = responce_create_user.json()["accessToken"]
#         # requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})


    @allure.description('Получение списка заказов неавторизованного пользователя')
    def test_unauthenticated_user(self,data_new):
        responce_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        list_of_orders = requests.get(urls.BASE_URL + urls.CREATE_ORDER_URL)

        assert 401 == list_of_orders.status_code and list_of_orders.json()["message"] == "You should be authorised"
        token = responce_create_user.json()["accessToken"]
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})

