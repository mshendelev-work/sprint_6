import allure

from src.constants import ConstantsURL
from src.locators.home_page_locators import HomePageLocators
from src.pages.base_page import BasePage


class HomePageSectionQuestion(BasePage):
    @allure.step('Наследование драйвера')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Возвращает значение ответа от требуемого вопроса')
    def main_page_questions(self, button, answer):
        self.navigate_to_url(ConstantsURL.HOME_URL)
        search_cookie = self.find_element(HomePageLocators.BUTTON_COOKIE)
        search_cookie.click()
        search_field = self.find_element(button)
        self.scroll_to_element(search_field)
        self.find_element_to_be_clickable(button)
        search_field.click()
        return self.find_element(answer).text
