import allure

from src.pages.home_page import HomePage


class TestOrderScooter:
    @allure.title('Проверка заказа самоката: позитивный сценарий, тестовый набор данных №1')
    def test_order_scooter_one_data(self, driver):
        home_page = HomePage(driver)
        get_button = home_page.make_an_order_scooter_one()
        assert get_button.is_displayed() is True, 'Button is not displayed'
        assert get_button.is_enabled() is True, 'Button is not enabled'

    @allure.title('Проверка заказа самоката: позитивный сценарий, тестовый набор данных №2')
    def test_order_scooter_second_data(self, driver):
        home_page = HomePage(driver)
        get_button = home_page.make_an_order_scooter_two()
        assert get_button.is_displayed() is True, 'Button is not displayed'
        assert get_button.is_enabled() is True, 'Button is not enabled'
