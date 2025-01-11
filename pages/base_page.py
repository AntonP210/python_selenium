from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except Exception as e:
            print(f"Error clicking element {by_locator}: {str(e)}")
            raise

    def send_keys(self, by_locator, text):
        try:
            self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)
        except Exception as e:
            print(f"Error sending keys to element {by_locator}: {str(e)}")
            raise

    def get_element_text(self, by_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            return element.text
        except Exception as e:
            print(f"Error getting text from element {by_locator}: {str(e)}")
            raise

    def is_visible(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except Exception as e:
            print(f"Error checking visibility of element {by_locator}: {str(e)}")
            return False