from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    ITEM_TITLE = (By.CSS_SELECTOR, ".basket-item .item-info a")
    CHECKOUT_BUTTON = (By.ID, "checkout-btn")

    def get_product_title(self):
        return self.get_text(self.ITEM_TITLE)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)