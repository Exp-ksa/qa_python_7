import allure
import generate_data

from api_methods.api_orders import Order

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Получение заказа по номеру')
class TestGetOrder:

    allure.story('Успешное получение заказа')
    @allure.title('Успешный запрос возвращает объект с заказом')
    def test_get_order_success_returns_order_object(self):
        order_payload = generate_data.generate_order()
        order_response = Order.create_order(order_payload)
        assert order_response.status_code == 201
        track = order_response.json()["track"]
        
        response = Order.get_order(track)
    
        assert response.status_code == 200
        assert 'order' in response.json()
        assert response.json()['order']["track"] == track

        Order.cancel_order(track)

    @allure.story('Ошибки при получении заказа')
    @allure.title('Запрос без номера заказа возвращает ошибку')
    def test_get_order_without_id_returns_error(self):
        response = Order.get_order("")
    
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Ошибки при получении заказа')
    @allure.title('Запрос с несуществующим заказом возвращает ошибку')
    def test_get_order_nonexistent_id_returns_error(self):
        response = Order.get_order(999999999)
    
        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"