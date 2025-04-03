from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIRST_NAME = By.XPATH, './/input[@placeholder="* Имя"]' # Поле для ввода имени
    INPUT_LAST_NAME = By.XPATH, './/input[@placeholder="* Фамилия"]' # Поле для ввода фамилии
    INPUT_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]' # Поле для ввода адреса
    INPUT_SUBWAY = By.XPATH,  './/input[@placeholder="* Станция метро"]' # Список со станциями метро
    CHOOSE_SUBWAY_STATION_CULTURE_PARK = By.XPATH, './/button[@value="13"]' # Станция метро «Парк Культуры»
    CHOOSE_SUBWAY_STATION_TULSKAYA = By.XPATH, './/button[@value="166"]' # Станция метро «Тульская»
    INPUT_PHONE_NUMBER = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]' # Поле для ввода
                                                                                        # номера телефона
    INPUT_DATE_ORDER = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]' # Поле для ввода даты заказа
    TEXT_MODAL_WINDOW = By.XPATH, './/div[@class="Order_Header__BZXOb"]' # Текст над модальным окном
    CHOOSE_RENTAL_PERIOD = By.XPATH, './/div[@class="Dropdown-placeholder"]' # Поле для выбора срока аренды
    CHOOSE_RENTAL_PERIOD_TWO_DAYS = By.XPATH, './/div[text()="двое суток"]'  # Поле для выбора срока аренды двое суток
    CHOOSE_RENTAL_PERIOD_FOUR_DAYS = By.XPATH, './/div[text()="двое суток"]'  # Поле для выбора срока аренды четверо суток
    CHOOSE_BLACK_COLOR_SCOOTER = By.XPATH, './/label[@class="Checkbox_Label__3wxSf"][1]' # Чек-бокс с черным цветом
    CHOOSE_BLACK_GREY_SCOOTER = By.XPATH, './/label[@class="Checkbox_Label__3wxSf"][2]'  # Чек-бокс с серым цветом
    INPUT_COMMENT_FOR_COURIER = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'  # Поле для ввода
                                                                                # комментария для курьера
    BUTTON_FURTHER = By.XPATH, ('.//div[@class="Order_NextButton__1_rCA"]/button'
                                '[@class="Button_Button__ra12g Button_Middle__1CSJM"]')  # Кнопка «Далее»
    BUTTON_ORDER = By.XPATH, ('.//div[@class="Order_Buttons__1xGrp"]//button'
                              '[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # Кнопка «Заказать»
    BUTTON_YES = By.XPATH, ('.//div[@class="Order_Modal__YZ-d3"]//'
                  'button[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # Кнопка «Заказать» в модальном окне
    BUTTON_VIEW_STATUS_ORDER = By.XPATH, ('.//div[@class="Order_NextButton__1_rCA"]/'
          'button[@class="Button_Button__ra12g Button_Middle__1CSJM"]') # Кнопка «Посмотреть статус» в модальном окне
    BUTTON_CANCEL_ORDER = By.XPATH, ('.//button[@class="Button_Button__ra12g Button_Middle__1CSJM'
                         ' Button_Inverted__3IF-i"]') # Кнопка «Отменить заказ» на странице заказа
