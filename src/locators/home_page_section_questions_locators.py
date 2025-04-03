from selenium.webdriver.common.by import By


class SectionQuestionsAbout:
    QUESTION_IS_HOW_MUCH = By.ID, 'accordion__heading-0' # Вопрос «Сколько это стоит? И как оплатить?»
    ANSWER_QUESTION_IS_HOW_MUCH = By.XPATH, './/div[@id="accordion__panel-0"]/p'
    QUESTION_OF_NUMBER_OF_SCOOTERS = By.ID, 'accordion__heading-1' # Вопрос «Хочу сразу несколько самокатов! Так можно?»
    ANSWER_QUESTION_OF_NUMBER_OF_SCOOTERS = By.XPATH, './/div[@id="accordion__panel-1"]/p'
    QUESTION_IS_RENTAL_TIME_CALCULATED = By.ID, 'accordion__heading-2' # Вопрос «Как рассчитывается время аренды?»
    ANSWER_QUESTION_IS_RENTAL_TIME_CALCULATED = By.XPATH, './/div[@id="accordion__panel-2"]/p'
    QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY = By.ID, 'accordion__heading-3' # Вопрос «Можно ли заказать самокат прямо
    # на сегодня?»
    ANSWER_QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY = By.XPATH, './/div[@id="accordion__panel-3"]/p'
    QUESTION_EXTEND_ORDER_OR_RETURN_SOONER = By.ID, 'accordion__heading-4' # Вопрос «Можно ли продлить заказ или
    # вернуть самокат раньше?»
    ANSWER_QUESTION_EXTEND_ORDER_OR_RETURN_SOONER = By.XPATH, './/div[@id="accordion__panel-4"]/p'
    QUESTION_CHARGER_WITH_SCOOTER = By.ID, 'accordion__heading-5' # Вопрос «Вы привозите зарядку вместе с самокатом?»
    ANSWER_QUESTION_CHARGER_WITH_SCOOTER = By.XPATH, './/div[@id="accordion__panel-5"]/p'
    QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER = By.ID, 'accordion__heading-6' # Вопрос «Можно ли отменить заказ?»
    ANSWER_QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER = By.XPATH, './/div[@id="accordion__panel-6"]/p'
    QUESTION_DELIVER_OUTSIDE_MOSCOW = By.ID, 'accordion__heading-7' # Вопрос «Я жизу за МКАДом, привезёте?»
    ANSWER_QUESTION_DELIVER_OUTSIDE_MOSCOW = By.XPATH, './/div[@id="accordion__panel-7"]/p'
