from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_BASKET = (By.XPATH, "//div[@id='desktop_qualifiedBuyBox']//input[@id='add-to-cart-button']")
    BASKET_LINK = (By.XPATH, "//div[@class='nav-right']//a[@id='nav-orders']")

    def add_to_cart(self):
        self.click_scroll(self.ADD_TO_BASKET)

    def go_to_cart(self):
        self.click(self.BASKET_LINK)