from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_YANDEX = By.XPATH, './/img[@src="/assets/ya.svg"]' # Кнопка «Яндекс»
    BUTTON_SCOOTER = By.XPATH, './/img[@src="/assets/scooter.svg"]' # Кнопка «Самокат»
    BUTTON_STATUS_ORDER = By.XPATH, './/button[@class="Header_Link__1TAG7"]' # Кнопка «Статус заказа»
    BUTTON_ORDER_HEADER = By.XPATH, ('.//div[@class="Header_Nav__AGCXC"]//button'
                    '[@class="Button_Button__ra12g"]') # Кнопка «Заказать» в хедере
