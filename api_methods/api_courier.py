import allure
import requests

from URL import URL

class Courier:

    @staticmethod
    @allure.step('Создание курьера с данными: {payload}')
    def create_courier(payload):
        return requests.post(URL.CREATE_COURIER_ENDPOINT, data=payload, verify=False)

    @staticmethod
    @allure.step('Логин курьера с данными: {payload}')
    def login_courier(payload):
        return requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload, verify=False)    
    
    @staticmethod
    @allure.step('Удаление курьера с ID: {courier_id}')
    def delete_courier(courier_id):
        url = f"{URL.CREATE_COURIER_ENDPOINT}/{courier_id}"
        return requests.delete(url, verify=False) 
    


    
