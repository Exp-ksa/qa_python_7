import allure

from api_methods.api_courier import Courier

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Авторизация курьера')
class TestLoginCourier:
    
    @allure.story('Успешная авторизация')
    @allure.title('Курьер может авторизоваться и получить ID')
    def test_courier_can_login_and_id_on_success(self, random_payload):
        Courier.create_courier(random_payload)
        login_response = Courier.login_courier(random_payload)
        assert login_response.status_code == 200
        assert 'id' in login_response.json()
        courier_id = login_response.json()["id"]
        Courier.delete_courier(courier_id)

    @allure.story('Ошибки при авторизации')
    @allure.title('Система вернёт ошибку, если неправильно указать пароль')
    def test_login_returns_error_for_invalid_password(self, random_payload):
        Courier.create_courier(random_payload)
        modified_payload = {**random_payload, "password": "wrong_password"}
        login_response = Courier.login_courier(modified_payload)
        assert login_response.status_code == 404
        assert login_response.json()["message"] == "Учетная запись не найдена"
        response = Courier.login_courier(random_payload)
        courier_id = response.json()["id"]
        Courier.delete_courier(courier_id)

    @allure.story('Ошибки при авторизации')
    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_returns_error_when_field_login_missing(self, random_payload):
        Courier.create_courier(random_payload)
        modified_payload = {**random_payload, "login": ""}
        login_response = Courier.login_courier(modified_payload)
        assert login_response.status_code == 400
        assert login_response.json()["message"] == "Недостаточно данных для входа"
        response = Courier.login_courier(random_payload)
        courier_id = response.json()["id"]
        Courier.delete_courier(courier_id)

    @allure.story('Ошибки при авторизации')
    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_returns_error_for_nonexistent_user(self, random_payload):
        login_response = Courier.login_courier(random_payload)
        assert login_response.status_code == 404
        assert login_response.json()["message"] == "Учетная запись не найдена"
        
    