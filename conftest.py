import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from urls import URLs
import allure


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и настройки Firefox драйвера
    """
    driver = None
    try:
        # Автоматическая установка и запуск драйвера
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        
        # Настройки браузера
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        # Открываем базовый URL
        driver.get(URLs.base_url)
        
        yield driver
        
    except Exception as e:
        # Сделать скриншот при ошибке
        if driver:
            allure.attach(driver.get_screenshot_as_png(), 
                         name="screenshot_on_error", 
                         attachment_type=allure.attachment_type.PNG)
        print(f"Ошибка при работе драйвера: {e}")
        if driver:
            driver.quit()
        raise
    
    finally:
        # Гарантированное закрытие драйвера
        if driver:
            driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для получения результатов теста и прикрепления скриншотов при падении
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Если тест упал, прикрепляем скриншот
        driver = None
        for item in item.funcargs.values():
            if isinstance(item, webdriver.Remote):
                driver = item
                break
        
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )