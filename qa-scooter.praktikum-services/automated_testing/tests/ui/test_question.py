import allure
import pytest

from automated_testing.data.urls import URLS
from automated_testing.pages.home_page import QuestionPage


class TestQuestion:

    @pytest.mark.parametrize(
        "number_question",
        [0, 1, 2, 3, 4, 5, 6]
    )
    @allure.title("Тест проверка появление ответа вопрос-ответ")
    def test_question(self, number_question, browser_def):
        quest = QuestionPage(browser_def)
        quest.open_url(URLS['ui']["/"])
        answer = quest.get_answer(number_question)
        status = quest.answer_status_hidden(answer)
        assert status
        question = quest.get_question(number_question)
        quest.scrol_to_element(question)
        quest.get_button_click(element=question)
        status = quest.answer_status_hidden(answer)
        assert status is None
