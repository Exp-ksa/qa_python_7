import pytest

from URL import URL
from api_methods.api_courier import Courier

from api_methods.api_orders import Order
import generate_data

@pytest.fixture(scope="function")
def random_payload():
    """Генерирует случайные данные курьера"""
    return generate_data.generate_courier_random()

# Удаление курьера
@pytest.fixture(scope="function")
def clear_courier(random_payload):
        
    yield random_payload
    
    # Очистка
    login_response = Courier.login_courier(random_payload)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        Courier.delete_courier(courier_id)

# Создаем и логинимся курьером
@pytest.fixture(scope="function")
def login_courier(random_payload):
    response = Courier.create_courier(random_payload)
    assert response.status_code == 201
    login_response = Courier.login_courier(random_payload)
    courier_id = login_response.json()["id"]   
    
    return courier_id

 # Создаём курьера и заказ для тестов
@pytest.fixture(scope="function")
def setup_data(random_payload):
    # Создаём курьера
    Courier.create_courier(random_payload)
        
    # Логинимся и получаем id курьера
    login_response = Courier.login_courier(random_payload)
    courier_id = login_response.json()["id"]
    
    order_payload = generate_data.generate_order()
    order_response = Order.create_order(order_payload)
    
    track = order_response.json()["track"]
    track_response = Order.get_order(track)
    
    order_id = track_response.json()["order"]["id"]
        
    yield {
            "courier_id": courier_id,
            "order_id": order_id,
            "order_payload": order_payload
        }
        
    # Удаляем тестовые данные
    Courier.delete_courier(courier_id)
