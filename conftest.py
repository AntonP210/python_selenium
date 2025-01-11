import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData

@pytest.fixture(scope="function")
def init_driver():
    if TestData.BROWSER == "chrome":
        options = webdriver.ChromeOptions()
        if not TestData.DEBUG_MODE:
            options.add_argument('--headless')
        service = Service(executable_path="drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise Exception("Browser not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(TestData.IMPLICIT_WAIT)
    yield driver
    driver.quit()