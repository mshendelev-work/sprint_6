import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
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

    def find_elements(self, locator, timeout=10):
        with allure.step(f'Find elements with locator: {locator}'):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
                )

    def click_element(self, locator, timeout=10):
        with allure.step(f'Click element with locator: {locator}'):
            self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        with allure.step(f'Enter text with locator: {locator}'):
            self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        with allure.step(f'Wait for element is visible and clickable with locator: {locator}'):
            return WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )

    def element_is_present(self, locator, timeout=10):
        with allure.step(f'Wait presence for element with locator: {locator}'):
            return WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )

    def scroll_to_element(self, locator, timeout=10):
        with allure.step(f'Scroll to element with locator: {locator}'):
            element = self.find_element(locator)
            ActionChains(self.driver, timeout).move_to_element(element).perform()
