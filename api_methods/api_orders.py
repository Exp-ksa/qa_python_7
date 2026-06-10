import json

import allure
import requests

from url import Url

class Order:

    @staticmethod
    @allure.step('Создание заказа с данными: {payload}')
    def create_order(payload):
        return requests.post(Url.CREATE_ORDER_ENDPOINT, json=payload, verify=False)

    @staticmethod
    @allure.step('Отмена заказа с треком: {payload}')
    def cancel_order(payload):
        return requests.put(Url.CANCEL_ORDER_ENDPOINT, params={"track": payload}, verify=False)    
    
    @staticmethod
    @allure.step('Принятие заказа {order_id} курьером {courier_id}')
    def accept_order(order_id, courier_id):
        url = f"{Url.ACCEPT_ORDERS_ENDPOINT}{order_id}"
        return requests.put(url, params={"courierId": courier_id}, verify=False) 
    
    @staticmethod
    @allure.step('Получение заказа по треку: {order_track}')
    def get_order(order_track):
        return requests.get(Url.TRACK_ORDER_ENDPOINT, params={"t": order_track}, verify=False)
    
    @staticmethod
    @allure.step('Получение списка заказов с параметрами: courierId={courierId}, nearestStation={nearestStation}, limit={limit}, page={page}')
    def get_list_order(courierId=None, nearestStation=None, limit=None, page=None):
        params = {}
        if courierId is not None:
            params["courierId"] = courierId
        if nearestStation is not None:
            params["nearestStation"] = json.dumps(nearestStation)
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        
        return requests.get(Url.CREATE_ORDER_ENDPOINT, params=params, verify=False)
    
    @staticmethod
    @allure.step('Завершение заказа {id_order}')
    def finish_order(id_order):
        url = f"{Url.FINISH_ORDER_ENDPOINT}/{id_order}"
        return requests.put(url, verify=False)
    