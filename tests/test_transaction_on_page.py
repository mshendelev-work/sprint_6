import allure

from src.constants import Constants
from src.locators.header_locators import HeaderLocators
from src.locators.home_page_locators import HomePageLocators
from src.pages.home_page import HomePage


class TestTransactionOnPage:
    @allure.title('Checking transition on home page')
    def test_transaction_on_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(Constants.HOME_URL)
        button_header_order = home_page.search_for_element(HeaderLocators.BUTTON_ORDER_HEADER)
        button_header_order.click()
        assert driver.current_url == Constants.ORDER_URL, 'User is not on ORDER_URL'
        button_header_scooter = home_page.search_for_element(HeaderLocators.BUTTON_SCOOTER)
        button_header_scooter.click()
        assert driver.current_url == Constants.HOME_URL, 'User is not on HOME_URL'

    @allure.title('Checking transition on yandex site')
    def test_transaction_on_yandex_site(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page(Constants.HOME_URL)
        button_header_order = home_page.search_for_element(HeaderLocators.BUTTON_YANDEX)
        button_header_order.click()
        home_page.switch_to_window()
        ICON_YANDEX = home_page.search_for_element(HomePageLocators.ICON_YANDEX_DZEN)
        home_page.wait_for_clickable(ICON_YANDEX)
        assert driver.current_url == Constants.YANDEX_URL, 'User is not on YANDEX_URL'
