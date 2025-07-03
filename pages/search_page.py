from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    BOOK_LANGUAGE_FILTER = (By.XPATH, "//span[@data-csa-c-content-id='p_n_feature_twenty-five_browse-bin/3291441011']//span[contains(text(), 'Russian')]")
    BOOK_FORMAT_FILTER = (By.XPATH, "//span[contains(text(), 'Paperback')]")
    BOOK = (By.XPATH, "//span[contains(text(), 'Программирование на Python: Для начинающих (Russian Edition)')]")

    def select_book(self):
        self.click(self.BOOK)

    def apply_filters(self):
        self.click_with_js(self.BOOK_LANGUAGE_FILTER)
        self.click_with_js(self.BOOK_FORMAT_FILTER)