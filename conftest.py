import pytest
from selenium import webdriver
from src.constants import Constants


# Запуск и закрытие драйвера
@pytest.fixture
def driver():
    """
    Фикстура для инициализации WebDriver.
    Запускает браузер перед тестами и закрывает его после завершения.
    """
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(Constants.HOME_URL)
    yield chrome
    chrome.quit()
