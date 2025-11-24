import allure
import sys
import os
from selenium.webdriver.common.by import By

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Абсолютный импорт вместо относительного
from pages.base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы Самоката"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"

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
        
        original_tab = self.driver.current_window_handle
        self.click(MainPageLocators.LOGO_YANDEX)
        
        self.wait_for_new_tab()
        new_tab = [tab for tab in self.driver.window_handles if tab != original_tab][0]
        self.driver.switch_to.window(new_tab)
        
        try:
            return "dzen.ru" in self.driver.current_url
        finally:
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

    @allure.step("Дождаться открытия новой вкладки")
    def wait_for_new_tab(self, timeout=10):
        """Ожидание открытия новой вкладки"""
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            if len(self.driver.window_handles) > 1:
                return True
            time.sleep(0.5)
        return False


# условие для предотвращения запуска напрямую
if __name__ == "__main__":
    print("Этот файл предназначен для импорта, а не для прямого запуска.")
    print("Запускайте тесты через: python -m pytest tests/")