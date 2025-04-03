import allure

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to_url(self, url):
        with allure.step('Open page'):
            self.driver.get(url)

    def find_element(self, locator, timeout=10):
        with allure.step(f'Find element with locator: {locator}'):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

    def find_element_to_click(self, locator, timeout=10):
        with allure.step(f'Click element with locator: {locator}'):
            self.find_element(locator, timeout).click()

    def find_element_enter_text(self, locator, text, timeout=10):
        with allure.step(f'Enter text with locator: {locator}'):
            self.find_element(locator, timeout).send_keys(text)

    def find_element_to_be_clickable(self, locator, timeout=10):
        with allure.step(f'Wait for the element to be clickable with locator: {locator}'):
            return WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
            )

    def scroll_to_element(self, locator):
        with allure.step(f'Scroll to element with locator: {locator}'):
            return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def switch_to_window(self):
        window_new = self.driver.window_handles[1]
        return self.driver.switch_to.window(window_new)
