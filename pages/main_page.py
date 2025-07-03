from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")
    SELECT_LOCATION = (By.XPATH, "//a[@id='nav-global-location-popover-link']")
    CODE_LOCATION = (By.XPATH, "//input[@id='GLUXZipUpdateInput']")
    APPLY_LOCATION = (By.XPATH, "//input[@aria-labelledby='GLUXZipUpdate-announce']")
    DONE_LOCATION = (By.XPATH, "//div[@class='a-popover-footer']//input[@id='GLUXConfirmClose']")

    def open(self):
        self.driver.get("https://www.bookdepository.com")

    def search_book(self, title):
        self.send_keys(self.SEARCH_INPUT, title)
        self.click(self.SEARCH_BUTTON)

    def select_location(self, code):
        self.click(self.SELECT_LOCATION)
        self.send_keys(self.CODE_LOCATION, code)
        self.click(self.APPLY_LOCATION)
        self.click(self.DONE_LOCATION)