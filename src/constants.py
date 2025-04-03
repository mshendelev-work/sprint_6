from faker import Faker


class Constants:
    HOME_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = f'{HOME_URL}order'
    YANDEX_URL = 'https://dzen.ru/?yredirect=true'
    fake = Faker('ru_RU')
    USER_DATA = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
    }
    PHONE_NUMBER_ONE = '79234141122'
    PHONE_NUMBER_SECOND = '79234142233'
    ADDRESS_ONE = 'ул. Петровка 32'
    ADDRESS_SECOND = 'переулок Сеченовский 8 стр.3'
    DATE_ONE = '23.10.2025'
    DATE_SECOND = '09.11.2025'
    COMMENT_FOR_COURIER_ONE = 'Хорошего дня!'
    COMMENT_FOR_COURIER_SECOND = 'Аккуратней на дорогах :)'
    TEXT_ANSWER_QUESTION_IS_HOW_MUCH = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_QUESTION_OF_NUMBER_OF_SCOOTERS = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с'
                                           ' друзьями, можете просто сделать несколько заказов — один за другим.')
    TEXT_ANSWER_QUESTION_IS_RENTAL_TIME_CALCULATED = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая'
        ' в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли'
                                                  ' самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    TEXT_ANSWER_QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_ANSWER_QUESTION_EXTEND_ORDER_OR_RETURN_SOONER = ('Пока что нет! Но если что-то срочное — всегда можно позвонить'
                                                          ' в поддержку по красивому номеру 1010.')
    TEXT_ANSWER_QUESTION_CHARGER_WITH_SCOOTER = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь'
                                 ' суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    TEXT_ANSWER_QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной'
                                                        ' записки тоже не попросим. Все же свои.')
    TEXT_ANSWER_QUESTION_DELIVER_OUTSIDE_MOSCOW = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
