import allure

from api_methods.api_orders import Order

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Получение списка заказов')
class TestListOrder:
    
    @allure.story('Получение всех заказов')
    @allure.title('Проверка, что тело ответа возвращает список заказов')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_orders_list_returns_orders_list(self):
        response = Order.get_list_order()
        
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)

    @allure.story('Фильтрация заказов по курьеру')
    @allure.title('Проверка получения заказов по ID курьера')
    def test_get_orders_list_returns_orders_courier_list(self, setup_data):
        data = setup_data
        order_id = data['order_id']
        courier_id = data['courier_id']
        Order.accept_order(order_id, courier_id)
        response = Order.get_list_order(courierId=courier_id)
        
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert response.json()["orders"][0]["courierId"] == courier_id       

    @allure.story('Фильтрация заказов по станции метро')
    @allure.title('Проверка получения заказов по станции метро')
    def test_get_orders_list_returns_orders_station_list(self, setup_data):
        data = setup_data
        order_id = data['order_id']
        courier_id = data['courier_id']
        metro_station = [str(data["order_payload"]["metroStation"])]
        accept_response = Order.accept_order(order_id, courier_id)
        
        assert accept_response.status_code == 200
        response = Order.get_list_order(nearestStation=metro_station)
        
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert response.json()["availableStations"][0]["number"] == metro_station[0]