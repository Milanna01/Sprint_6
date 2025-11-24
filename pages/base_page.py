from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    """Базовый класс Page Object со всеми основными взаимодействиями"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Скролл к элементу {locator}")
    def scroll_to(self, locator):
        """Прокрутить страницу к элементу"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    @allure.step("Кликнуть на {locator}")
    def click(self, locator):
        """Кликнуть на элемент с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step("Ввести '{text}' в поле {locator}")
    def type(self, locator, text):
        """Очистить поле и ввести текст"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return element

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        """Получить видимый текст элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Получить значение атрибута '{attribute}' элемента {locator}")
    def get_attribute(self, locator, attribute):
        """Получить значение атрибута элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        """Переключиться на новую вкладку и вернуть handle исходной"""
        original_tab = self.driver.current_window_handle
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        
        for handle in self.driver.window_handles:
            if handle != original_tab:
                self.driver.switch_to.window(handle)
                break
        
        # Ждем загрузки контента новой вкладки
        self.wait.until(lambda driver: driver.current_url not in ['about:blank', ''])
        return original_tab

    @allure.step("Вернуться к исходной вкладке")
    def switch_to_original_tab(self, original_tab):
        """Вернуться к исходной вкладке"""
        self.driver.switch_to.window(original_tab)

    @allure.step("Закрыть текущую вкладку")
    def close_tab(self):
        """Закрыть текущую вкладку"""
        self.driver.close()

    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator, timeout=10):
        """Проверить, что элемент видим"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator, timeout=10):
        """Дождаться, пока элемент станет невидимым"""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        """Открыть указанный URL"""
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL страницы"""
        url = self.driver.current_url
        allure.attach(url, name="Current URL", attachment_type=allure.attachment_type.TEXT)
        return url

    @allure.step("Получить заголовок страницы")
    def get_page_title(self):
        """Получить заголовок страницы"""
        title = self.driver.title
        allure.attach(title, name="Page Title", attachment_type=allure.attachment_type.TEXT)
        return title

    @allure.step("Обновить страницу")
    def refresh(self):
        """Обновить текущую страницу"""
        self.driver.refresh()

    @allure.step("Выполнить JavaScript: {script}")
    def execute_script(self, script, *args):
        """Выполнить JavaScript код"""
        return self.driver.execute_script(script, *args)

    @allure.step("Сделать скриншот и прикрепить к отчету")
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к Allure отчету"""
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        return screenshot

    @allure.step("Выбрать опцию из выпадающего списка по тексту")
    def select_dropdown_by_text(self, dropdown_locator, option_text):
        """Выбрать опцию из выпадающего списка по видимому тексту"""
        from selenium.webdriver.support.ui import Select
        dropdown = self.wait.until(EC.element_to_be_clickable(dropdown_locator))
        select = Select(dropdown)
        select.select_by_visible_text(option_text)

    @allure.step("Дождаться загрузки элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        """Дождаться появления элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, timeout=10):
        """Дождаться, пока элемент станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Прикрепить текст к отчету: {name}")
    def attach_text(self, text, name="text_attachment"):
        """Прикрепить произвольный текст к Allure отчету"""
        allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)

    @allure.step("Прикрепить HTML к отчету: {name}")
    def attach_html(self, html, name="html_attachment"):
        """Прикрепить HTML код к Allure отчету"""
        allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML)

    @allure.step("Получить исходный код страницы")
    def get_page_source(self):
        """Получить исходный код страницы и прикрепить к отчету"""
        page_source = self.driver.page_source
        allure.attach(page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)
        return page_source

    @allure.step("Переключиться на frame: {frame_locator}")
    def switch_to_frame(self, frame_locator):
        """Переключиться на указанный frame"""
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
        return frame

    @allure.step("Вернуться к основному контенту")
    def switch_to_default_content(self):
        """Вернуться к основному контенту страницы"""
        self.driver.switch_to.default_content()

    @allure.step("Принять alert")
    def accept_alert(self):
        """Принять alert диалог"""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    @allure.step("Отклонить alert")
    def dismiss_alert(self):
        """Отклонить alert диалог"""
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    @allure.step("Получить текст alert")
    def get_alert_text(self):
        """Получить текст из alert диалога"""
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        allure.attach(text, name="Alert Text", attachment_type=allure.attachment_type.TEXT)
        return text