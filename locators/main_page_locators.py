from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_MAIN = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    
    # Логотипы
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # Куки
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    
    # FAQ секция
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    FAQ_ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel') and @aria-hidden='false']")
    
    # Вопросы FAQ
    QUESTION_COST = (By.ID, "accordion__heading-0")
    QUESTION_MULTIPLE_SCOOTERS = (By.ID, "accordion__heading-1")
    QUESTION_RENTAL_TIME = (By.ID, "accordion__heading-2")
    QUESTION_TODAY_ORDER = (By.ID, "accordion__heading-3")
    QUESTION_EXTEND_RETURN = (By.ID, "accordion__heading-4")
    QUESTION_CHARGING = (By.ID, "accordion__heading-5")
    QUESTION_CANCEL_ORDER = (By.ID, "accordion__heading-6")
    QUESTION_MKAD = (By.ID, "accordion__heading-7")
    
    # Ответы FAQ
    ANSWER_COST = (By.ID, "accordion__panel-0")
    ANSWER_MULTIPLE_SCOOTERS = (By.ID, "accordion__panel-1")
    ANSWER_RENTAL_TIME = (By.ID, "accordion__panel-2")
    ANSWER_TODAY_ORDER = (By.ID, "accordion__panel-3")
    ANSWER_EXTEND_RETURN = (By.ID, "accordion__panel-4")
    ANSWER_CHARGING = (By.ID, "accordion__panel-5")
    ANSWER_CANCEL_ORDER = (By.ID, "accordion__panel-6")
    ANSWER_MKAD = (By.ID, "accordion__panel-7")
    
    # Блок статуса заказа (после успешного оформления)
    ORDER_STATUS_SECTION = (By.CLASS_NAME, "Order_Modal__YZ-d3")