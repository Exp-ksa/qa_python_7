import allure

import generate_data
from api_methods.api_courier import Courier

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Удаление курьера')
class TestDeleteCourier:
    
    @allure.story('Успешное удаление курьера')
    @allure.title('Успешный запрос возвращает {{"ok": true}}')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_courier_successful_returns_ok_true(self, create_login_courier):
        delete_response = Courier.delete_courier(create_login_courier)
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.story('Ошибки при удалении курьера')
    @allure.title('Если отправить запрос без id, вернётся ошибка')
    def test_delete_courier_without_id_returns_error(self):
        delete_response = Courier.delete_courier('')
        assert delete_response.status_code == 400
        assert delete_response.json()["message"] == "Недостаточно данных для удаления курьера"

    @allure.story('Ошибки при удалении курьера')
    @allure.title('Если отправить запрос с несуществующим id, вернётся ошибка')
    def test_delete_courier_nonexistent_id_returns_error(self): 
        delete_response = Courier.delete_courier(generate_data.generate_fake_id_courier())
        assert delete_response.status_code == 404 
        assert delete_response.json()["message"] == "Курьера с таким id нет"