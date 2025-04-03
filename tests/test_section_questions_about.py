import allure

from src.locators.home_page_locators import HomePageLocators
from src.locators.home_page_section_questions_locators import SectionQuestionsAbout
from src.pages.home_page_section_questions import HomePageSectionQuestion
from src.constants import Constants


class TestSectionQuestionsAbout:
    @allure.title('Checking answer to questions number one')
    def test_get_answer_questions_one(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_IS_HOW_MUCH)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_IS_HOW_MUCH).text ==
                Constants.TEXT_ANSWER_QUESTION_IS_HOW_MUCH)

    @allure.title('Checking answer to questions number two')
    def test_get_answer_questions_two(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_OF_NUMBER_OF_SCOOTERS)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_OF_NUMBER_OF_SCOOTERS).text ==
                Constants.TEXT_QUESTION_OF_NUMBER_OF_SCOOTERS)

    @allure.title('Checking answer to questions number three')
    def test_get_answer_questions_three(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_IS_RENTAL_TIME_CALCULATED)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_IS_RENTAL_TIME_CALCULATED).text ==
                Constants.TEXT_ANSWER_QUESTION_IS_RENTAL_TIME_CALCULATED)

    @allure.title('Checking answer to questions number four')
    def test_get_answer_questions_four(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY).text
                == Constants.TEXT_ANSWER_QUESTION_IS_POSSIBLE_ORDER_RIGHT_AWAY)

    @allure.title('Checking answer to questions number five')
    def test_get_answer_questions_five(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_EXTEND_ORDER_OR_RETURN_SOONER)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_EXTEND_ORDER_OR_RETURN_SOONER).text
                == Constants.TEXT_ANSWER_QUESTION_EXTEND_ORDER_OR_RETURN_SOONER)

    @allure.title('Checking answer to questions number six')
    def test_get_answer_questions_six(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_CHARGER_WITH_SCOOTER)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_CHARGER_WITH_SCOOTER).text
                == Constants.TEXT_ANSWER_QUESTION_CHARGER_WITH_SCOOTER)

    @allure.title('Checking answer to questions number seven')
    def test_get_answer_questions_seven(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER).text
                == Constants.TEXT_ANSWER_QUESTION_IS_POSSIBLE_TO_CANCEL_ORDER)

    @allure.title('Checking answer to questions number eight')
    def test_get_answer_questions_eight(self, driver):
        get_answer = HomePageSectionQuestion(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.click_for_element(HomePageLocators.BUTTON_COOKIE)
        search_field = get_answer.search_for_element(SectionQuestionsAbout.QUESTION_DELIVER_OUTSIDE_MOSCOW)
        get_answer.scroll_to_question(search_field)
        get_answer.wait_for_clickable(search_field)
        search_field.click()

        assert (get_answer.search_for_element(SectionQuestionsAbout.ANSWER_QUESTION_DELIVER_OUTSIDE_MOSCOW).text
                == Constants.TEXT_ANSWER_QUESTION_DELIVER_OUTSIDE_MOSCOW)
