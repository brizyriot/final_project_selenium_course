import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.page_load_strategy = "eager"
    # options.add_argument('--headless=new')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()