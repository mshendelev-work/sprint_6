import allure

from src.locators.home_page_section_questions_locators import SectionQuestionsAbout
from src.pages.home_page_section_questions import HomePageLocators
from src.constants import Constants


class TestSectionQuestionsAbout:
    @allure.title('Checking answer to questions')
    def test_get_answer_questions(self, driver):
        get_answer = HomePageLocators(driver)
        get_answer.open_home_page(Constants.HOME_URL)
        get_answer.scroll_to_question(SectionQuestionsAbout.QUESTION_IS_HOW_MUCH)
        get_answer.click_question(SectionQuestionsAbout.QUESTION_IS_HOW_MUCH)
        get_answer.wait_for_answer(SectionQuestionsAbout.ANSWER_QUESTION_IS_HOW_MUCH)

        assert (get_answer.get_text_question(SectionQuestionsAbout.ANSWER_QUESTION_IS_HOW_MUCH) ==
                Constants.TEXT_ANSWER_QUESTION_IS_HOW_MUCH)
