import allure

from api_methods.api_orders import Order

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Принятие заказа')
class TestAcceptOrder:
    
    @allure.story('Успешное принятие заказа')
    @allure.title('Успешный запрос возвращает {"ok":true}')
    def test_accept_order_success_returns_ok_true(self, setup_data):
        data = setup_data
        order_id = data['order_id']
        courier_id = data['courier_id']
        response = Order.accept_order(order_id, courier_id)
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.story('Ошибки при принятии заказа')
    @allure.title('Если не передать id курьера, запрос вернёт ошибку')
    def test_accept_order_without_courier_id_returns_error(self, setup_data):
        data = setup_data
        order_id = data['order_id']
        courier_id = ""
        response = Order.accept_order(order_id, courier_id)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Ошибки при принятии заказа')
    @allure.title('Если передать неверный id курьера, запрос вернёт ошибку')
    def test_accept_order_invalid_courier_id_returns_error(self, setup_data):
        data = setup_data
        order_id = data['order_id']
        courier_id = '99999999'
        response = Order.accept_order(order_id, courier_id)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.story('Ошибки при принятии заказа')
    @allure.title('Если не передать id заказа, запрос вернёт ошибку')
    def test_accept_order_without_order_id_returns_error(self, setup_data):
        data = setup_data
        courier_id = data['courier_id']
        response = Order.accept_order("", courier_id)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Ошибки при принятии заказа')
    @allure.title('Если передать неверный id заказа, запрос вернёт ошибку')
    def test_accept_order_invalid_order_id_returns_error(self, setup_data):
        data = setup_data
        order_id = '999999999'
        courier_id = data['courier_id']
        response = Order.accept_order(order_id, courier_id)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"