import allure
import requests
import urls
class TestCreateOrder:

    @allure.description('Создание заказа с авторизацией и ингредиентами')
    def test_authenticated_with_ingredients(self, data_new):
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        token = response_create_user.json()["accessToken"]
        del data_new["name"]
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, data={"ingredients": "61c0c5a71d1f82001bdaaa6d"}, headers={"Autorization": token})
        assert 200 == responce_create_order.status_code and responce_create_order.json()["name"] == "Флюоресцентный бургер" and responce_create_order.json()["order"] != []
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})



    @allure.description('Создание заказа с авторизацией и без ингредиентов')
    def test_authenticated_without_ingredients(self, data_new):
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        token = response_create_user.json()["accessToken"]
        del data_new["name"]
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Autorization": token})
        assert 400 == responce_create_order.status_code and responce_create_order.json()["success"] == False and responce_create_order.json()["message"] == "Ingredient ids must be provided"
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})


    @allure.description('Создание заказа без авторизации и с ингредиентами')
    def test_unauthenticated_with_ingredients(self):
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, data={"ingredients": "61c0c5a71d1f82001bdaaa6d"})
        assert 200 == responce_create_order.status_code and responce_create_order.json()["name"] == "Флюоресцентный бургер"


    @allure.description('Создание заказа без авторизации и без ингредиентов')
    def test_unauthenticated_without_ingredients(self):
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL)
        assert 400 == responce_create_order.status_code and responce_create_order.json()["message"] == "Ingredient ids must be provided"


    @allure.description('Создание заказа без авторизации и невалиднным хешем')
    def test_unauthenticated_with_bad_hesh(self):
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, data={"ingredients": "01bdaaa6d"})
        assert 500 == responce_create_order.status_code and responce_create_order.reason == "Internal Server Error"


    @allure.description('Создание заказа c авторизаией и невалиднным хешем')
    def test_authenticated_with_bad_hesh(self, data_new):
        response_create_user = requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, data=data_new)
        token = response_create_user.json()["accessToken"]
        del data_new["name"]
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Autorization": token}, data={"ingredients": "01bdaaa6d"})
        assert 500 == responce_create_order.status_code and responce_create_order.reason == "Internal Server Error"
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=data_new, headers={"Autorization": token})



