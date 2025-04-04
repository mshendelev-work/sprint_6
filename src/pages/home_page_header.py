import allure

from src.constants import ConstantsURL
from src.locators.header_locators import HeaderLocators
from src.locators.home_page_locators import HomePageLocators
from src.pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Наследование драйвера')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Возвращает значение текущей страницы Самоката')
    def home_page_scooter(self):
        self.navigate_to_url(ConstantsURL.HOME_URL)
        button_header_order = self.find_element(HeaderLocators.BUTTON_ORDER_HEADER)
        button_header_order.click()
        assert self.current_url() == ConstantsURL.ORDER_URL, 'User is not on ORDER_URL'
        button_header_scooter = self.find_element(HeaderLocators.BUTTON_SCOOTER)
        button_header_scooter.click()
        return self.current_url()

    @allure.step('Возвращает значение текущей страницы Яндекс Дзена')
    def home_page_yandex_dzen(self):
        self.navigate_to_url(ConstantsURL.HOME_URL)
        button_header_order = self.find_element(HeaderLocators.BUTTON_YANDEX)
        button_header_order.click()
        self.switch_to_window()
        self.find_element(HomePageLocators.ICON_YANDEX_DZEN)
        self.find_element_to_be_clickable(HomePageLocators.ICON_YANDEX_DZEN)
        return self.current_url()
