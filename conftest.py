import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from src.constants import ConstantsURL


# Запуск и закрытие драйвера
@pytest.fixture
def driver():

    firefox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    firefox.maximize_window()
    firefox.get(ConstantsURL.HOME_URL)
    yield firefox
    firefox.quit()
