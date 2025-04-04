from selenium.webdriver.common.by import By


class SectionQuestionsAbout:
    QUESTION_ONE_BUTTON = By.ID, 'accordion__heading-0' # Вопрос «Сколько это стоит? И как оплатить?»
    ANSWER_QUESTION_ONE = By.XPATH, './/div[@id="accordion__panel-0"]/p'
    QUESTION_TWO_BUTTON = By.ID, 'accordion__heading-1' # Вопрос «Хочу сразу несколько самокатов! Так можно?»
    ANSWER_QUESTION_TWO = By.XPATH, './/div[@id="accordion__panel-1"]/p'
    QUESTION_THREE_BUTTON = By.ID, 'accordion__heading-2' # Вопрос «Как рассчитывается время аренды?»
    ANSWER_QUESTION_THREE = By.XPATH, './/div[@id="accordion__panel-2"]/p'
    QUESTION_FOUR_BUTTON = By.ID, 'accordion__heading-3' # Вопрос «Можно ли заказать самокат прямо на сегодня?»
    ANSWER_QUESTION_FOUR = By.XPATH, './/div[@id="accordion__panel-3"]/p'
    QUESTION_FIVE_BUTTON = By.ID, 'accordion__heading-4' # Вопрос «Можно ли продлить заказ или вернуть самокат раньше?»
    ANSWER_QUESTION_FIVE = By.XPATH, './/div[@id="accordion__panel-4"]/p'
    QUESTION_SIX_BUTTON = By.ID, 'accordion__heading-5' # Вопрос «Вы привозите зарядку вместе с самокатом?»
    ANSWER_QUESTION_SIX = By.XPATH, './/div[@id="accordion__panel-5"]/p'
    QUESTION_SEVEN_BUTTON = By.ID, 'accordion__heading-6' # Вопрос «Можно ли отменить заказ?»
    ANSWER_QUESTION_SEVEN = By.XPATH, './/div[@id="accordion__panel-6"]/p'
    QUESTION_EIGHT_BUTTON = By.ID, 'accordion__heading-7' # Вопрос «Я жизу за МКАДом, привезёте?»
    ANSWER_QUESTION_EIGHT = By.XPATH, './/div[@id="accordion__panel-7"]/p'
