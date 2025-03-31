import faker


class Constants:
    HOME_URL = 'https://qa-scooter.praktikum-services.ru/'
    LOGIN_URL = f'{HOME_URL}login'
    REGISTRATION_URL = f'{HOME_URL}register'
    RECOVERY_PASSWORD_URL = f'{HOME_URL}forgot-password'
    PERSONAL_ACCOUNT_PAGE = f'{HOME_URL}account/profile'
    CORRECT_USER_DATA = {
        'name': faker.Faker().name(),
        'email': faker.Faker().email(),
        'password': faker.Faker().password()
    }
    INCORRECT_USER_PASSWORD = {
        'name': faker.Faker().name(),
        'email': faker.Faker().email(),
        'password': '12345'
    }
    BASIC_USER_DATA = {
        'name': 'Михаил',
        'email': 'shendelev_19@gmail.com',
        'password': 'yandex_practicum'
    }
    TEXT_ANSWER_QUESTION_IS_HOW_MUCH = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
