from time import sleep

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
            search_page.select_first_book()

        with allure.step("3. Добавление в корзину"):
            product_page = ProductPage(browser)
            product_page.add_to_cart()
            product_page.go_to_cart()
            sleep(3)

        with allure.step("4. Проверка корзины"):
            cart_page = CartPage(browser)
            assert "Python" in cart_page.get_product_title()
            cart_page.proceed_to_checkout()