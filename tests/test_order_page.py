import allure
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import DataUser1, DataUser2


@allure.epic("QA Scooter")
@allure.feature("Оформление заказа")
class TestOrderFlow:
    """Тесты процесса оформления заказа"""

    @allure.title("Оформление заказа через верхнюю кнопку 'Заказать'")
    @allure.description("Проверка полного цикла заказа с данными первого пользователя")
    @allure.story("Успешное оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("scooter", "order", "smoke")
    def test_order_via_top_button_success(self, driver):
        """Полный цикл заказа через верхнюю кнопку"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        user_data = DataUser1()
        
        # Подготовка
        main_page.open()
        main_page.accept_cookies()
        
        # Начало заказа
        main_page.start_order("верхнюю")
        
        # Заполнение форм заказа
        order_page.fill_first_form(user_data)
        order_page.fill_second_form(user_data)
        
        # Проверка успешности заказа
        assert order_page.check_status_button_displayed(), "Не отображается подтверждение заказа"

    @allure.title("Оформление заказа через нижнюю кнопку 'Заказать'")
    @allure.description("Проверка полного цикла заказа с данными второго пользователя")
    @allure.story("Успешное оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("scooter", "order", "smoke")
    def test_order_via_bottom_button_success(self, driver):
        """Полный цикл заказа через нижнюю кнопку"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        user_data = DataUser2()
        
        # Подготовка
        main_page.open()
        main_page.accept_cookies()
        
        # Начало заказа (альтернативный путь)
        main_page.start_order("нижнюю")
        
        # Заполнение форм заказа
        order_page.fill_first_form(user_data)
        order_page.fill_second_form(user_data)
        
        # Проверка успешности заказа
        assert order_page.check_status_button_displayed(), "Не отображается подтверждение заказа"