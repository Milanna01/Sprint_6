import allure
import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.base_page import BasePage
from urls import URLs
from locators.main_page_locators import MainPageLocators


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
        if self.is_visible(MainPageLocators.COOKIE_ACCEPT_BUTTON):
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Начать заказ через верхнюю кнопку")
    def start_order_from_header(self):
        """Начать заказ через кнопку в хедере"""
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Начать заказ через нижнюю кнопку")
    def start_order_from_main(self):
        """Начать заказ через кнопку в основной части страницы"""
        self.scroll_to(MainPageLocators.ORDER_BUTTON_MAIN)
        self.click(MainPageLocators.ORDER_BUTTON_MAIN)

    @allure.step("Начать заказ через указанную кнопку")
    def start_order_by_locator(self, button_locator, scroll_to_button=False):
        """
        Универсальный метод для начала заказа через указанную кнопку
        
        Args:
            button_locator: Локатор кнопки заказа
            scroll_to_button: Нужно ли скроллить к кнопке (по умолчанию False)
        """
        if scroll_to_button:
            self.scroll_to(button_locator)
        self.click(button_locator)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Перейти к разделу FAQ")
    def go_to_faq_section(self):
        self.scroll_to(MainPageLocators.FAQ_SECTION)

    @allure.step("Раскрыть вопрос FAQ: {question_name}")
    def expand_faq_question(self, question_name):
        question_locator = getattr(MainPageLocators, f"QUESTION_{question_name.upper()}")
        self.scroll_to(question_locator)
        self.click(question_locator)

    @allure.step("Получить текст ответа на вопрос: {question_name}")
    def get_faq_answer(self, question_name):
        answer_locator = getattr(MainPageLocators, f"ANSWER_{question_name.upper()}")
        return self.get_text(answer_locator)

    @allure.step("Проверить, что открыта главная страница")
    def is_main_page_active(self):
        return self.get_current_url() == self.url

    @allure.step("Проверить переход на Дзен")
    def check_yandex_redirect(self):
        """Проверка редиректа на Дзен через логотип Яндекс"""
        # Получаем текущее количество окон и handle текущей вкладки
        original_windows_count = self.get_window_handles_count()
        original_tab = self.get_current_window_handle()
        
        # Кликаем на логотип Яндекс
        self.click(MainPageLocators.LOGO_YANDEX)
        
        # Ждем открытия нового окна/вкладки
        self.wait_for_new_window(original_windows_count)
        
        # Переключаемся на новую вкладку
        self.switch_to_new_window(original_tab)
        
        try:
            # Ждем загрузки страницы Дзена и проверяем URL
            self.wait_for_url_contains("dzen.ru")
            return "dzen.ru" in self.get_current_url()
        finally:
            # Закрываем новую вкладку и возвращаемся на исходную
            self.close_tab()
            self.switch_to_original_tab(original_tab)

    @allure.step("Получить текст вопроса FAQ: {question_name}")
    def get_faq_question_text(self, question_name):
        """Получить текст вопроса"""
        question_locator = getattr(MainPageLocators, f"QUESTION_{question_name.upper()}")
        return self.get_text(question_locator)

    @allure.step("Проверить видимость ответа на вопрос: {question_name}")
    def is_faq_answer_visible(self, question_name):
        answer_locator = getattr(MainPageLocators, f"ANSWER_{question_name.upper()}")
        return self.is_visible(answer_locator)