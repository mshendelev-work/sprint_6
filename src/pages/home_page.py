import allure

from src.constants import ConstantsURL
from src.locators.home_page_locators import HomePageLocators
from src.pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('Наследование драйвера')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход к форме заказа')
    def proceed_to_order_form(self):
        self.navigate_to_url(ConstantsURL.HOME_URL)
        search_cookie = self.find_element(HomePageLocators.BUTTON_COOKIE)
        search_cookie.click()
        button_order = self.find_element(HomePageLocators.BUTTON_ORDER_HOME_PAGE)
        self.scroll_to_element(button_order)
        self.find_element_to_be_clickable(button_order)
        button_order.click()
