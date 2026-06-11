import allure

from api_methods.api_courier import Courier

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Авторизация курьера')
class TestLoginCourier:
    
    @allure.story('Успешная авторизация')
    @allure.title('Курьер может авторизоваться и получить ID')
    def test_courier_can_login_and_id_on_success(self, clear_courier):
        Courier.create_courier(clear_courier)
        login_response = Courier.login_courier(clear_courier)
        assert login_response.status_code == 200
        assert 'id' in login_response.json()
        

    @allure.story('Ошибки при авторизации')
    @allure.title('Система вернёт ошибку, если неправильно указать пароль')
    def test_login_returns_error_for_invalid_password(self, clear_courier):
        Courier.create_courier(clear_courier)
        modified_payload = {**clear_courier, "password": "wrong_password"}
        login_response = Courier.login_courier(modified_payload)
        assert login_response.status_code == 404
        assert login_response.json()["message"] == "Учетная запись не найдена"
        

    @allure.story('Ошибки при авторизации')
    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_returns_error_when_field_login_missing(self, clear_courier):
        Courier.create_courier(clear_courier)
        modified_payload = {**clear_courier, "login": ""}
        login_response = Courier.login_courier(modified_payload)
        assert login_response.status_code == 400
        assert login_response.json()["message"] == "Недостаточно данных для входа"
        

    @allure.story('Ошибки при авторизации')
    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_returns_error_for_nonexistent_user(self, random_payload):
        login_response = Courier.login_courier(random_payload)
        assert login_response.status_code == 404
        assert login_response.json()["message"] == "Учетная запись не найдена"
        
    