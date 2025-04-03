from selenium.webdriver.common.by import By


class HomePageLocators:
    BUTTON_COOKIE = By.XPATH, './/button[@class="App_CookieButton__3cvqF"]' # Кнопка для принятия cookie
    BUTTON_ORDER_HOME_PAGE = By.XPATH, ('.//div[@class="Home_FinishButton__1_cWm"]/button'
                    '[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # Кнопка «Заказать» на главной странице
    ICON_YANDEX_DZEN = By.XPATH, ('.//div[@class="dzen-layout--desktop-base-header__logoContainer-pu dzen-layout-'
                    '-desktop-base-header__isMorda-2n"]') # Иконка Яндекс Дзена на главной странице Яндекса
