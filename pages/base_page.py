from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def click_scroll(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def click_with_js(self, locator):
        try:
            self.click(locator)
        except Exception as e:
            print(f"Regular click failed, trying JS click: {e}")
            element = self.find(locator)
            self.driver.execute_script("arguments[0].click();", element)


    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text