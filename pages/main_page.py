import allure
import sys
import os
import time
from selenium.webdriver.support import expected_conditions as EC

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.base_page import BasePage
from urls import URLs


class MainPage(BasePage):
    """Page Object для главной страницы Самоката"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = URLs.scooter_url

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(self.url)

    @allure.step("Принять куки")
    def accept_cookies(self):
        from locators.main_page_locators import MainPageLocators
        if self.is_visible(MainPageLocators.COOKIE_ACCEPT_BUTTON):
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Начать заказ через {button_type} кнопку")
    def start_order(self, button_type="верхнюю"):
        from locators.main_page_locators import MainPageLocators
        if button_type == "верхнюю":
            self.click(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.scroll_to(MainPageLocators.ORDER_BUTTON_MAIN)
            self.click(MainPageLocators.ORDER_BUTTON_MAIN)

    @allure.step("Кликнуть на логотип {logo_type}")
    def click_logo(self, logo_type="Самоката"):
        from locators.main_page_locators import MainPageLocators
        if logo_type == "Самоката":
            self.click(MainPageLocators.LOGO_SCOOTER)
        else:
            self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Перейти к разделу FAQ")
    def go_to_faq_section(self):
        from locators.main_page_locators import MainPageLocators
        self.scroll_to(MainPageLocators.FAQ_SECTION)

    @allure.step("Раскрыть вопрос FAQ: {question_name}")
    def expand_faq_question(self, question_name):
        from locators.main_page_locators import MainPageLocators
        question_locator = getattr(MainPageLocators, f"QUESTION_{question_name.upper()}")
        self.scroll_to(question_locator)
        self.click(question_locator)

    @allure.step("Получить текст ответа на вопрос: {question_name}")
    def get_faq_answer(self, question_name):
        from locators.main_page_locators import MainPageLocators
        answer_locator = getattr(MainPageLocators, f"ANSWER_{question_name.upper()}")
        return self.get_text(answer_locator)

    @allure.step("Проверить, что открыта главная страница")
    def is_main_page_active(self):
        return self.get_current_url() == self.url

    @allure.step("Проверить переход на Дзен")
    def check_yandex_redirect(self):
        """Проверка редиректа на Дзен через логотип Яндекс"""
        from locators.main_page_locators import MainPageLocators
        
        # Запоминаем текущее количество окон
        original_windows_count = len(self.driver.window_handles)
        original_tab = self.driver.current_window_handle
        
        self.click(MainPageLocators.LOGO_YANDEX)
        
        # Ждем открытия нового окна/вкладки
        self.wait.until(EC.number_of_windows_to_be(original_windows_count + 1))
        
        # Находим новую вкладку
        new_tab = [tab for tab in self.driver.window_handles if tab != original_tab][0]
        self.driver.switch_to.window(new_tab)
        
        try:
            # Ждем загрузки страницы и проверяем URL
            self.wait.until(EC.url_contains("dzen.ru"))
            return "dzen.ru" in self.driver.current_url
        finally:
            # Закрываем новую вкладку и возвращаемся на исходную
            self.driver.close()
            self.driver.switch_to.window(original_tab)

    @allure.step("Получить текст вопроса FAQ: {question_name}")
    def get_faq_question_text(self, question_name):
        """Получить текст вопроса"""
        from locators.main_page_locators import MainPageLocators
        question_locator = getattr(MainPageLocators, f"QUESTION_{question_name.upper()}")
        return self.get_text(question_locator)

    @allure.step("Проверить видимость ответа на вопрос: {question_name}")
    def is_faq_answer_visible(self, question_name):
        from locators.main_page_locators import MainPageLocators
        answer_locator = getattr(MainPageLocators, f"ANSWER_{question_name.upper()}")
        return self.is_visible(answer_locator)