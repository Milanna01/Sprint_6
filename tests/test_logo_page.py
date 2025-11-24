import allure
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.main_page import MainPage


@allure.epic("QA Scooter")
@allure.feature("Навигация")
class TestLogoNavigation:
    """Тесты навигации через логотипы"""

    @allure.title("Логотип Самокат возвращает на главную страницу")
    @allure.description("Проверка возврата на главную через логотип Самокат")
    @allure.story("Навигация по логотипам")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("scooter", "navigation", "logo")
    def test_scooter_logo_returns_to_main_page(self, driver):
        """Проверка возврата на главную через логотип Самокат"""
        main_page = MainPage(driver)
        
        # Открываем и настраиваем страницу
        main_page.open()
        main_page.accept_cookies()
        
        # Уходим с главной страницы (начинаем заказ)
        main_page.start_order("верхнюю")
        
        # Возвращаемся через логотип
        main_page.click_logo("Самоката")
        
        # Проверяем возврат
        assert main_page.is_main_page_active(), "Не удалось вернуться на главную страницу"

    @allure.title("Логотип Яндекс открывает Дзен в новой вкладке")
    @allure.description("Проверка перехода на Дзен через логотип Яндекс")
    @allure.story("Навигация по логотипам")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("scooter", "navigation", "yandex")
    def test_yandex_logo_opens_dzen(self, driver):
        """Проверка перехода на Дзен через логотип Яндекс"""
        main_page = MainPage(driver)
        
        # Открываем и настраиваем страницу
        main_page.open()
        main_page.accept_cookies()
        
        # Кликаем на Яндекс логотип и проверяем переход
        is_dzen = main_page.check_yandex_redirect()
        assert is_dzen, "Дзен не открылся в новой вкладке"