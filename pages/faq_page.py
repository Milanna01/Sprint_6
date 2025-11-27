import allure
import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Импорты на уровне модуля
from pages.base_page import BasePage
from locators.faq_locators import FAQLocators


class QuestionPage(BasePage):
    """Page Object для работы с FAQ вопросами"""

    @allure.step("Проскроллить к разделу FAQ")
    def scroll_to_faq_section(self):
        """Проскроллить к разделу часто задаваемых вопросов"""
        self.scroll_to(FAQLocators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос #{index}")
    def click_question(self, index):
        """
        Кликнуть на вопрос по индексу
        
        Args:
            index (int): Индекс вопроса (0-7)
        """
        # Используем методы из BasePage вместо прямого вызова WebDriverWait
        self.scroll_to(FAQLocators.question[index])
        self.click_element(FAQLocators.question[index])

    @allure.step("Получить текст вопроса #{index}")
    def get_question_text(self, index):
        """
        Получить текст вопроса по индексу
        
        Args:
            index (int): Индекс вопроса (0-7)
            
        Returns:
            str: Текст вопроса
        """
        return self.get_element_text(FAQLocators.question[index])

    @allure.step("Получить текст ответа #{index}")
    def get_answer_text(self, index):
        """
        Получить текст ответа по индексу
        
        Args:
            index (int): Индекс ответа (0-7)
            
        Returns:
            str: Текст ответа
        """
        return self.get_element_text(FAQLocators.answer[index])

    @allure.step("Проверить видимость ответа #{index}")
    def is_answer_visible(self, index):
        """
        Проверить видимость ответа по индексу
        
        Args:
            index (int): Индекс ответа (0-7)
            
        Returns:
            bool: True если ответ видим
        """
        return self.is_element_visible(FAQLocators.answer[index])

    @allure.step("Раскрыть все вопросы FAQ и проверить ответы")
    def expand_all_questions(self):
        """Раскрыть все вопросы и проверить что ответы отображаются"""
        for i in range(8):
            self.click_question(i)
            assert self.is_answer_visible(i), f"Ответ на вопрос {i} не отображается"