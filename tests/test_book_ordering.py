import re

import pytest
import allure
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@allure.feature("Оформление заказа книги")
class TestBookOrdering:
    @pytest.mark.usefixtures("browser")
    def test_book_ordering_flow(self, browser):
        with allure.step("1. Поиск книги"):
            main_page = MainPage(browser)
            main_page.open()
            main_page.search_book("Python programming")
            main_page.select_location("00501")

        with allure.step("2. Применение фильтров"):
            search_page = SearchPage(browser)
            search_page.apply_filters()
            search_page.select_book()

        with allure.step("3. Добавление в корзину"):
            product_page = ProductPage(browser)
            price = product_page.get_product_price()
            price_normalized = re.search(r'\$\d+\.\d+', price).group()
            print(f"Цена товара: {price_normalized}")
            product_page.add_to_cart()
            product_page.go_to_cart()

        with allure.step("4. Проверка корзины"):
            cart_page = CartPage(browser)
            assert "Python" in cart_page.get_product_title(), "Название товара не содержит 'Python'"
            price_cart = cart_page.get_product_price_cart()
            price_cart_normalized = re.search(r'\$\d+\.\d+', price_cart).group()
            print(f"Цена товара в корзине: {price_cart_normalized}")
            assert price_normalized == price_cart_normalized, f'Цены не совпадают: {price} != {price_cart}'