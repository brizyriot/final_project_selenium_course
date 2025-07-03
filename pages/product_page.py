from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//input[@id='add-to-cart-button' and @title='Add to Shopping Cart']")
    CART_BUTTON = (By.XPATH, "//*[@id='sw-gtc']/span/a")
    PRICE_PRODUCT = (By.XPATH, "//*[@id='a-autoid-2-announce']/span[2]/span")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)

    def get_product_price(self):
        """Получает цену товара через JavaScript поиск по span элементам"""
        try:
            price_script = """
                return [...document.querySelectorAll('span')]
                    .find(el => el.textContent.includes('$') || el.textContent.includes('€') || el.textContent.includes('₽'))
                    ?.textContent?.trim() || '';
                """
            price = self.driver.execute_script(price_script)

            if not price:
                raise ValueError("Цена не найдена через JS поиск по span элементам")

            return price.strip()

        except Exception as e:
            self.driver.save_screenshot("price_error.png")
            raise Exception(f"Ошибка при получении цены: {str(e)}")

