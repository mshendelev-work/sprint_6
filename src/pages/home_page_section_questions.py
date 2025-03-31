from src.pages.base_page import BasePage


class HomePageLocators(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, url):
        self.navigate_to_url(url)

    def scroll_to_question(self, locator):
        self.scroll_to_element(locator)

    def click_question(self, locator):
        self.click_element(locator)

    def wait_for_answer(self, locator):
        self.wait_for_element_visible(locator)

    def get_text_question(self, locator):
        return self.find_element(locator).text
