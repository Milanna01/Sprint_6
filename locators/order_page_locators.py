from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""
    
    # Первая форма - персональные данные
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая форма - данные аренды
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопки оформления
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Статус заказа
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    # Модальное окно подтверждения
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    
    # Станции метро (пример для часто используемых)
    METRO_STATION_OPTION = (By.CLASS_NAME, "select-search__option")
    
    # Периоды аренды
    RENTAL_PERIOD_OPTION = (By.CLASS_NAME, "Dropdown-option")