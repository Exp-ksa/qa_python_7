import allure

from api_methods.api_courier import Courier

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Создание курьера')
class TestCreateCourier:
    
    @allure.story('Успешное создание курьера')
    @allure.title('Курьера можно создать')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_courier_can_be_created(self, clear_courier):
        response = Courier.create_courier(clear_courier)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    @allure.story('Ошибки при создании курьера')
    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_courier_cannot_be_created_twice(self, clear_courier):
        
        response = Courier.create_courier(clear_courier)
        assert response.status_code == 201
    
        # Пытаемся создать такого же
        response = Courier.create_courier(clear_courier)  
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"
        
    @allure.story('Ошибки при создании курьера')
    @allure.title('Если нет login, запрос возвращает ошибку')
    def test_create_courier_missing_field_login_returns_error(self, clear_courier):
        del clear_courier["login"]
        response = Courier.create_courier(clear_courier)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.story('Ошибки при создании курьера')
    @allure.title('Если нет password, запрос возвращает ошибку')
    def test_create_courier_missing_field_password_returns_error(self, random_payload):
        del random_payload["password"]
        response = Courier.create_courier(random_payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"