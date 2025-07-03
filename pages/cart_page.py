from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    ITEM_TITLE = (By.XPATH, "//span[contains(@class, 'a-truncate-cut') and contains(text(), 'Python')]")
    PRODUCT_PRICE_CART = (By.XPATH, "//*[@id='sc-subtotal-amount-activecart']/span")

    def get_product_title(self):
        return self.get_text(self.ITEM_TITLE)

    def get_product_price_cart(self):
        return self.get_text(self.PRODUCT_PRICE_CART)
