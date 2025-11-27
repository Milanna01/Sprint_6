import allure
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Абсолютный импорт вместо относительного
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Page Object для страницы оформления заказа"""

    @allure.step('Выбрать станцию метро: {station_name}')
    def select_station(self, station_name):
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click(station_locator)

    @allure.step('Проверить отображение кнопки статуса заказа')
    def check_status_button_displayed(self):
        from locators.order_page_locators import OrderPageLocators
        return self.is_visible(OrderPageLocators.ORDER_STATUS_BUTTON)

    @allure.step('Заполнить первую часть формы заказа')
    def fill_first_form(self, user_data):
        from locators.order_page_locators import OrderPageLocators
        
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT))
        
        # Заполнение персональных данных
        self.type(OrderPageLocators.NAME_INPUT, user_data.name)
        self.type(OrderPageLocators.LAST_NAME_INPUT, user_data.surname)
        self.type(OrderPageLocators.ADDRESS_INPUT, user_data.address)
        
        # Выбор станции метро
        self.click(OrderPageLocators.METRO_STATION_INPUT)
        self.type(OrderPageLocators.METRO_STATION_INPUT, user_data.station_name)
        self.select_station(user_data.station_name)
        
        # Заполнение контактных данных
        self.type(OrderPageLocators.PHONE_INPUT, user_data.telephone)
        
        # Переход ко второй форме
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую часть формы заказа')
    def fill_second_form(self, user_data):
        from locators.order_page_locators import OrderPageLocators
        
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_INPUT))
        
        # Заполнение даты
        self.type(OrderPageLocators.DELIVERY_DATE_INPUT, user_data.date)
        
        # Выбор цвета
        if 'чёрный' in user_data.color:
            self.click(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        else:
            self.click(OrderPageLocators.GREY_COLOR_CHECKBOX)
        
        # Выбор срока аренды
        self.select_rental_period(user_data.period)
        
        # Заполнение комментария
        self.type(OrderPageLocators.COMMENT_INPUT, user_data.comment)
        
        # Оформление заказа
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.confirm_order()

    @allure.step('Выбрать срок аренды: {period}')
    def select_rental_period(self, period):
        from locators.order_page_locators import OrderPageLocators
        
        self.click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
        self.click(period_locator)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        from locators.order_page_locators import OrderPageLocators
        
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.CONFIRM_ORDER_BUTTON))
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Полное оформление заказа')
    def complete_order(self, user_data):
        """Полный процесс оформления заказа"""
        self.fill_first_form(user_data)
        self.fill_second_form(user_data)
        return self.check_status_button_displayed()


