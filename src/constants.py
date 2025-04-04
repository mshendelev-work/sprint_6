from faker import Faker


class ConstantsURL:
    HOME_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = f'{HOME_URL}order'
    YANDEX_URL = 'https://dzen.ru/?yredirect=true'


class ConstantsUserData:
    fake = Faker('ru_RU')
    USER_DATA = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name()
    }
    PHONE_NUMBER_ONE = '79234141122'
    PHONE_NUMBER_SECOND = '79234142233'
    ADDRESS_ONE = 'ул. Петровка 32'
    ADDRESS_SECOND = 'переулок Сеченовский 8 стр.3'
    DATE_ONE = '23.10.2025'
    DATE_SECOND = '09.11.2025'
    COMMENT_FOR_COURIER_ONE = 'Хорошего дня!'
    COMMENT_FOR_COURIER_SECOND = 'Аккуратней на дорогах :)'


class ConstantsForAnswer:
    TEXT_ANSWER_QUESTION_ONE = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_ANSWER_QUESTION_TWO = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями,'
                                ' можете просто сделать несколько заказов — один за другим.')
    TEXT_ANSWER_QUESTION_THREE = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая'
        ' в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли'
                                                  ' самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    TEXT_ANSWER_QUESTION_FOUR = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_ANSWER_QUESTION_FIVE = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по'
                                                                                ' красивому номеру 1010.')
    TEXT_ANSWER_QUESTION_SIX = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже'
                                        ' если будете кататься без передышек и во сне. Зарядка не понадобится.')
    TEXT_ANSWER_QUESTION_SEVEN = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не'
                                                                                    ' попросим. Все же свои.')
    TEXT_ANSWER_QUESTION_EIGHT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
