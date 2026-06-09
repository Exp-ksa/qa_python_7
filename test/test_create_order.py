import pytest
import allure
from api_methods.api_orders import Order
from data import DataOrder
import generate_data

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Создание заказа')
class TestCreateOrder:
    
    @allure.story('Создание заказа с разными цветами')
    @allure.title('Создание заказа с параметрами: {payload}')
    @pytest.mark.parametrize('payload', [
                                        DataOrder.order[0], 
                                        DataOrder.order[1], 
                                        DataOrder.order[2], 
                                        DataOrder.order[3]
                                        ])
    def test_create_order(self, payload):
        response = Order.create_order(payload)
        assert response.status_code == 201
        assert 'track' in response.json()
        
        track = response.json()["track"]
        Order.cancel_order(track)

    @allure.story('Создание заказа с рандомными данными')
    @allure.title('Создание заказа с сгенерированными данными')
    def test_create_generate_data(self):
        order_payload = generate_data.generate_order()
        order_response = Order.create_order(order_payload)
        assert order_response.status_code == 201
        assert 'track' in order_response.json()

        track = order_response.json()["track"]
        Order.cancel_order(track)
