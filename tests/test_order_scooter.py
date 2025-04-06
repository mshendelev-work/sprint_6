import allure

from src.pages.home_page import HomePage
from src.pages.order_page import OrderPage


class TestOrderScooter:
    @allure.title('Проверка заказа самоката: позитивный сценарий, тестовый набор данных №1')
    def test_order_scooter_one_data(self, driver):
        home_page = HomePage(driver)
        home_page.proceed_to_order_form()
        order_page = OrderPage(driver)
        order_page.filling_first_order_page_first_data()
        order_page.filling_second_order_page_first_data()
        get_button = order_page.filling_second_order_page()
        assert get_button.is_displayed() is True, 'Button is not displayed'
        assert get_button.is_enabled() is True, 'Button is not enabled'

    @allure.title('Проверка заказа самоката: позитивный сценарий, тестовый набор данных №2')
    def test_order_scooter_second_data(self, driver):
        home_page = HomePage(driver)
        home_page.proceed_to_order_form()
        order_page = OrderPage(driver)
        order_page.filling_first_order_page_second_data()
        order_page.filling_second_order_page_second_data()
        get_button = order_page.filling_second_order_page()
        assert get_button.is_displayed() is True, 'Button is not displayed'
        assert get_button.is_enabled() is True, 'Button is not enabled'
