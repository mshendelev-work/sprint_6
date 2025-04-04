import allure
import pytest

from src.constants import ConstantsForAnswer
from src.locators.home_page_section_questions_locators import SectionQuestionsAbout
from src.pages.home_page_section_questions import HomePageSectionQuestion


class TestMainQuestions:
    @allure.title('Проверяет список вопросов/ответов на главной странице')
    @pytest.mark.parametrize('button, answer, expected_result',
         [(SectionQuestionsAbout.QUESTION_ONE_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_ONE,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_ONE),
          (SectionQuestionsAbout.QUESTION_TWO_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_TWO,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_TWO),
          (SectionQuestionsAbout.QUESTION_THREE_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_THREE,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_THREE),
          (SectionQuestionsAbout.QUESTION_FOUR_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_FOUR,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_FOUR),
          (SectionQuestionsAbout.QUESTION_FIVE_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_FIVE,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_FIVE),
          (SectionQuestionsAbout.QUESTION_SIX_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_SIX,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_SIX),
          (SectionQuestionsAbout.QUESTION_SEVEN_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_SEVEN,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_SEVEN),
          (SectionQuestionsAbout.QUESTION_EIGHT_BUTTON, SectionQuestionsAbout.ANSWER_QUESTION_EIGHT,
           ConstantsForAnswer.TEXT_ANSWER_QUESTION_EIGHT)])
    def test_questions(self, button, answer, expected_result, driver):
        main_page = HomePageSectionQuestion(driver)
        get_answer = main_page.main_page_questions(button, answer)
        assert get_answer == expected_result
