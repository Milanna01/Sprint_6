# QA Python Sprint 6 - Автоматизация тестирования сервиса "Яндекс.Самокат"

📋 О проекте
Автоматизированные тесты для веб-сайта заказа самокатов QA Scooter. Проект включает в себя полный набор тестовых сценариев для проверки функциональности приложения.

🏗️ Структура проекта
text
Sprint_6/
├── 📊 allure_results/                 # Allure отчеты о тестировании
│   ├── categories.json
│   ├── executor.json
│   ├── history/
│   └── ... (результаты тестов)
├── 🐍 __pycache__/                    # Кэш-файлы Python
├── 🧩 pages/                          # Page Object Model
│   ├── __init__.py
│   ├── base_page.py                   # 🔧 Базовый класс
│   ├── main_page.py                   # 🏠 Главная страница
│   ├── order_page.py                  # 🛒 Страница заказа
│   └── faq_page.py                    # ❓ Страница FAQ
├── 🔍 locators/                       # Локаторы элементов
│   ├── __init__.py
│   ├── main_page_locators.py          # 🎯 Локаторы главной
│   ├── order_page_locators.py         # 📝 Локаторы заказа
│   └── faq_locators.py                # 💬 Локаторы FAQ
├── ✅ tests/                          # Тестовые сценарии
│   ├── __init__.py
│   ├── test_faq_page.py               # 🧪 Тесты FAQ
│   ├── test_order_page.py             # 🧪 Тесты заказа
│   └── test_logo_navigation.py        # 🧪 Тесты навигации
├── ⚙️  conftest.py                    # Фикстуры Pytest
├── 📝 data.py                         # Тестовые данные
├── 🌐 urls.py                         # URL адреса
├── 📦 requirements.txt                # Зависимости
├── 🚫 .gitignore                      # Игнорируемые файлы
└── 📖 README.md                       # Документация

🚀 Быстрый старт
Предварительные требования
Python 3.9 или выше

pip (менеджер пакетов Python)

Браузер Firefox (для запуска тестов)

Установка
Клонируйте репозиторий:

bash
git clone <your-repo-url>
cd Sprint_6
Установите зависимости:

bash
pip install -r requirements.txt
Установите Allure Framework:

bash
# Для Windows (через scoop)
scoop install allure

# Для Mac
brew install allure

# Для Linux
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure
🧪 Запуск тестов
Запуск всех тестов с генерацией отчета
bash
python -m pytest tests/ --alluredir=allure_results -v
Запуск отдельных тестовых наборов
bash
# Только тесты заказов
python -m pytest tests/test_order_page.py -v

# Только тесты FAQ
python -m pytest tests/test_faq_page.py -v

# Только тесты навигации
python -m pytest tests/test_logo_navigation.py -v
Просмотр отчетов Allure
bash
# Генерация HTML отчета
allure generate allure_results -o allure-report --clean

# Запуск отчета в браузере
allure open allure-report

# Или запуск сервера Allure
allure serve allure_results
📊 Тестовые сценарии
🛒 Оформление заказа
✅ Оформление заказа через верхнюю кнопку "Заказать"

✅ Оформление заказа через нижнюю кнопку "Заказать"

✅ Заполнение всех обязательных полей формы

✅ Выбор станции метро из выпадающего списка

✅ Выбор срока аренды и цвета самоката

❓ FAQ раздел
✅ Проверка всех 8 вопросов в аккордеоне

✅ Соответствие текстов вопросов и ответов ожидаемым значениям

✅ Раскрытие/скрытие ответов при клике на вопросы

🧭 Навигация
✅ Возврат на главную страницу через логотип "Самокат"

✅ Переход на Dzen через логотип "Яндекс"

✅ Работа кнопок принятия cookies

🔧 Технологии
Python 3.9+ - основной язык программирования

Selenium WebDriver - автоматизация браузера

Pytest - фреймворк для тестирования

Allure Framework - создание отчетов о тестировании

Page Object Pattern - архитектура проекта

📝 Особенности реализации
Page Object Model - чистое разделение тестов и локаторов

Явные ожидания - стабильность тестов при изменении скорости загрузки

Allure отчеты - детальная информация о каждом шаге теста

Параметризованные тесты - эффективное тестирование разных сценариев

Автоматическая установка драйверов - через webdriver-manager

🗂️ Файлы и директории
Основные файлы:
conftest.py - настройка фикстуры драйвера и обработка скриншотов при падении тестов

data.py - тестовые данные пользователей (DataUser1, DataUser2) и вопросы/ответы FAQ

urls.py - константы с URL адресами приложения

Результаты тестирования:
allure_results/ - содержит сырые данные для генерации Allure отчетов

__pycache__/ - автоматически сгенерированные кэш-файлы Python для ускорения импорта



