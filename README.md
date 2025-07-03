# Тестовый проект для AliExpress

## Цель
Автоматизация проверки добавления товара в корзину через фильтры.

## Технологии
- Python 3.10+
- Selenium 4
- Pytest
- Allure/HTML-отчёты

## Запуск
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   
2. Запустите тест:
   ```bash
   pytest tests/test_add_to_cart.py

3. Откройте отчёт:
   ```bash
   allure serve reports/allure
