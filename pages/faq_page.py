import allure
import sys
import os
from selenium.webdriver.support import expected_conditions as EC

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.base_page import BasePage


class QuestionPage(BasePage):
    """Page Object для работы с FAQ вопросами"""

    @allure.step("Проскроллить к разделу FAQ")
    def scroll_to_faq_section(self):
        from locators.faq_locators import FAQLocators
        self.scroll_to(FAQLocators.FAQ_SECTION)

    @allure.step("Кликнуть на вопрос #{index}")
    def click_question(self, index):
        from locators.faq_locators import FAQLocators
        self.scroll_to(FAQLocators.question[index])
        self.click(FAQLocators.question[index])

    @allure.step("Получить текст вопроса #{index}")
    def get_question_text(self, index):
        from locators.faq_locators import FAQLocators
        self.wait.until(EC.visibility_of_element_located(FAQLocators.question[index]))
        return self.get_text(FAQLocators.question[index])

    @allure.step("Получить текст ответа #{index}")
    def get_answer_text(self, index):
        from locators.faq_locators import FAQLocators
        self.wait.until(EC.visibility_of_element_located(FAQLocators.answer[index]))
        return self.get_text(FAQLocators.answer[index])


# условие для предотвращения запуска напрямую
if __name__ == "__main__":
    print("Этот файл предназначен для импорта, а не для прямого запуска.")
    print("Запускайте тесты через: python -m pytest tests/test_faq_page.py")