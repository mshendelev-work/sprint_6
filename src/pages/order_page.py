from src.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, url):
        return self.navigate_to_url(url)

    def search_for_element(self, locator):
        return self.find_element(locator)

    def click_for_element(self, locator):
        return self.find_element_to_click(locator)

    def scroll_to_station(self, locator):
        return self.scroll_to_element(locator)

    def wait_for_clickable(self, locator):
        return self.find_element_to_be_clickable(locator)
