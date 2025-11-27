from selenium.webdriver.common.by import By


class FAQLocators:
    """Локаторы для раздела FAQ"""
    
    # Основной раздел FAQ
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    
    # Вопросы (по индексам 0-7)
    QUESTION_0 = (By.ID, "accordion__heading-0")
    QUESTION_1 = (By.ID, "accordion__heading-1") 
    QUESTION_2 = (By.ID, "accordion__heading-2")
    QUESTION_3 = (By.ID, "accordion__heading-3")
    QUESTION_4 = (By.ID, "accordion__heading-4")
    QUESTION_5 = (By.ID, "accordion__heading-5")
    QUESTION_6 = (By.ID, "accordion__heading-6")
    QUESTION_7 = (By.ID, "accordion__heading-7")
    
    # Ответы (по индексам 0-7)
    ANSWER_0 = (By.ID, "accordion__panel-0")
    ANSWER_1 = (By.ID, "accordion__panel-1")
    ANSWER_2 = (By.ID, "accordion__panel-2")
    ANSWER_3 = (By.ID, "accordion__panel-3")
    ANSWER_4 = (By.ID, "accordion__panel-4")
    ANSWER_5 = (By.ID, "accordion__panel-5")
    ANSWER_6 = (By.ID, "accordion__panel-6")
    ANSWER_7 = (By.ID, "accordion__panel-7")
    
    # Список вопросов для удобства итерации
    question = [QUESTION_0, QUESTION_1, QUESTION_2, QUESTION_3, 
                QUESTION_4, QUESTION_5, QUESTION_6, QUESTION_7]
    
    # Список ответов для удобства итерации
    answer = [ANSWER_0, ANSWER_1, ANSWER_2, ANSWER_3,
              ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7]