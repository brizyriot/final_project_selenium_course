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
            assert main_page.is_page_opened(), "Главная страница не загрузилась"
            main_page.search_book("Python programming")
            main_page.select_location("00501")
            assert main_page.is_location_set("00501"), "Локация не установилась"

        with allure.step("2. Применение фильтров и выбор книги"):
            search_page = SearchPage(browser)
            assert search_page.is_search_results_visible(), "Результаты поиска не отображаются"
            search_page.apply_filters()
            assert search_page.are_filters_applied(), "Фильтры не применились"
            search_page.select_first_book()
            sleep(2)  # Ожидание загрузки страницы товара

        with allure.step("3. Добавление в корзину"):
            product_page = ProductPage(browser)
            assert product_page.is_product_page_loaded(), "Страница товара не загрузилась"
            initial_cart_count = product_page.get_cart_items_count()
            product_page.add_to_cart()
            sleep(2)  # Ожидание обновления корзины
            assert product_page.get_cart_items_count() > initial_cart_count, "Товар не добавился в корзину"
            product_page.go_to_cart()
            sleep(3)

        with allure.step("4. Проверка корзины и оформление заказа"):
            cart_page = CartPage(browser)
            assert cart_page.is_cart_page_loaded(), "Страница корзины не загрузилась"
            product_title = cart_page.get_product_title()
            assert "Python" in product_title, f"В корзине неверный товар: {product_title}"
            assert cart_page.is_checkout_button_visible(), "Кнопка оформления заказа не видна"
            cart_page.proceed_to_checkout()
            sleep(2)  # Ожидание перехода на страницу оформления