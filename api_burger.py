import allure
import requests
import urls
import data

class CreateUser:
    @allure.step('Вызов ручки создания пользователя')
    def create_user(self, body):
        return requests.post(urls.BASE_URL + urls.AUTH_REGISTER_USER_URL, json=body)



# class ChangeDataUser:
#
#
# class CreateOrder:
#
# class GetOrderOfUser:
#
# class LoginUser:
