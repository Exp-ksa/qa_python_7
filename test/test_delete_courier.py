import allure

from data import DataCourier
from api_methods.api_courier import Courier

@allure.epic('Тестирование сервиса аренды самокатов')
@allure.feature('Удаление курьера')
class TestDeleteCourier:
    
    @allure.story('Успешное удаление курьера')
    @allure.title('Успешный запрос возвращает {{"ok": true}}')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_courier_successful_returns_ok_true(self, login_courier):
        delete_response = Courier.delete_courier(login_courier)
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
        delete_response = Courier.delete_courier(DataCourier.courier_id)
        assert delete_response.status_code == 404 
        assert delete_response.json()["message"] == "Курьера с таким id нет"