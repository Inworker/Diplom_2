import allure
import requests
import helper
import urls


class TestCreateOrder:

    @allure.description('Создание заказа с авторизацией и ингредиентами')
    def test_authenticated_with_ingredients(self, data_new3):
        response_create_user, payload = data_new3
        token = response_create_user.json()["accessToken"]
        response_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL,
                                              data=helper.CreateCurrierData.FIRST_INGREDIENT,
                                              headers={"Authorization": token})
        assert 200 == response_create_order.status_code and response_create_order.json()[
            "name"] == "Флюоресцентный бургер" and response_create_order.json()["order"] != []
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=payload, headers={"Authorization": token})

    @allure.description('Создание заказа с авторизацией и без ингредиентов')
    def test_authenticated_without_ingredients(self, data_new3):
        response_create_user, payload = data_new3
        token = response_create_user.json()["accessToken"]
        response_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token})
        assert 400 == response_create_order.status_code and response_create_order.json()["success"] == False and \
               response_create_order.json()["message"] == "Ingredient ids must be provided"
        requests.delete(urls.BASE_URL + urls.AUTH_USER_URL, data=payload, headers={"Authorization": token})

    @allure.description('Создание заказа без авторизации и с ингредиентами')
    def test_unauthenticated_with_ingredients(self):
        response_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL,
                                              data=helper.CreateCurrierData.FIRST_INGREDIENT)
        assert 200 == response_create_order.status_code and response_create_order.json()[
            "name"] == "Флюоресцентный бургер"

    @allure.description('Создание заказа без авторизации и без ингредиентов')
    def test_unauthenticated_without_ingredients(self):
        response_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL)
        assert 400 == response_create_order.status_code and response_create_order.json()[
            "message"] == "Ingredient ids must be provided"

    @allure.description('Создание заказа без авторизации и невалиднным хешем')
    def test_unauthenticated_with_bad_hesh(self):
        responce_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL,
                                              data=helper.CreateCurrierData.BAD_INGREDIENT)
        assert 500 == responce_create_order.status_code and responce_create_order.reason == "Internal Server Error"

    @allure.description('Создание заказа c авторизаией и невалиднным хешем')
    def test_authenticated_with_bad_hesh(self, data_new3):
        response_create_user, payload = data_new3
        token = response_create_user.json()["accessToken"]
        response_create_order = requests.post(urls.BASE_URL + urls.CREATE_ORDER_URL, headers={"Authorization": token},
                                              data=helper.CreateCurrierData.BAD_INGREDIENT)
        assert 500 == response_create_order.status_code and response_create_order.reason == "Internal Server Error"
