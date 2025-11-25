import allure
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.faq_page import QuestionPage
from data import QuestionsAndAnswers


@allure.epic("QA Scooter")
@allure.feature("FAQ раздел")
class TestFaqPages:
    """Тесты раздела часто задаваемых вопросов"""

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Тест проверяет, что все вопросы и ответы соответствуют заданным в QuestionsAndAnswers')
    @allure.story("Проверка вопросов и ответов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("scooter", "faq", "content")
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_answers_true(self, driver, index):
        """
        Проверка соответствия вопросов и ответов на сайте QA Scooter
        """
        question_page = QuestionPage(driver)
        
        # Открываем главную страницу
        driver.get("https://qa-scooter.praktikum-services.ru/")
        
        # Скролл к разделу FAQ
        question_page.scroll_to_faq_section()
        
        # Клик по конкретному вопросу
        question_page.click_question(index)
        
        # Получаем актуальные данные со страницы
        actual_question = question_page.get_question_text(index)
        actual_answer = question_page.get_answer_text(index)
        
        # Ожидаемые данные из тестовых данных
        expected_question, expected_answer = QuestionsAndAnswers.test_data_question_answers[index]
        
        # Проверки с подробными сообщениями
        assert actual_question == expected_question, \
            f"Вопрос {index}: ожидался '{expected_question}', но получен '{actual_question}'"
        
        assert actual_answer == expected_answer, \
            f"Ответ {index}: ожидался '{expected_answer}', но получен '{actual_answer}'"