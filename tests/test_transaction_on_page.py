import allure

from src.constants import ConstantsURL
from src.pages.home_page_header import HomePageHeader


class TestTransactionOnPage:
    @allure.title('Проверка редиректа на главную страницу самоката')
    def test_transaction_on_home_page(self, driver):
        home_page = HomePageHeader(driver)
        current_url = home_page.home_page_scooter()
        assert current_url == ConstantsURL.HOME_URL, 'User is not on HOME_URL'

    @allure.title('Проверка редиректа на страницу Яндекс Дзена')
    def test_transaction_on_yandex_site(self, driver):
        home_page = HomePageHeader(driver)
        current_url = home_page.home_page_yandex_dzen()
        assert current_url == ConstantsURL.YANDEX_URL, 'User is not on YANDEX_URL'
