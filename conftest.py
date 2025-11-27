import pytest
import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from urls import URLs
import allure

# Настройка логирования
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и настройки Firefox драйвера
    """
    driver = None
    
    try:
        # Автоматическая установка и запуск драйвера Firefox
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

        # Настройки браузера для оптимального тестирования
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Открываем базовый URL приложения для тестирования
        driver.get(URLs.base_url)

        # Передаем драйвер в тест
        yield driver

    except Exception as e:
        # Логируем ошибку и делаем скриншот
        logger.error(f"Ошибка при работе драйвера: {e}", exc_info=True)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(), 
                name="screenshot_on_error", 
                attachment_type=allure.attachment_type.PNG
            )
        # Пробрасываем исключение дальше
        raise
        
    finally:
        # Гарантированное закрытие драйвера после выполнения теста
        if driver:
            driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для получения результатов теста и прикрепления скриншотов при падении
    """
    outcome = yield
    report = outcome.get_result()
    
    # Если тест упал во время выполнения (не во время setup/teardown)
    if report.when == "call" and report.failed:
        # Ищем экземпляр драйвера среди аргументов теста
        driver = None
        for arg in item.funcargs.values():
            if isinstance(arg, webdriver.Remote):
                driver = arg
                break
        
        # делаем скриншот и прикрепляем к Allure
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
            # Логируем информацию о падении теста
            logger.warning(f"Тест {item.name} упал, скриншот сохранен в отчете Allure")