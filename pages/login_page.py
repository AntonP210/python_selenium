from .base_page import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    CART_ICON = (By.XPATH, '//*[@data-icon="shopping-cart"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_cart_icon(self):
        return self.is_visible(self.CART_ICON)
    
    def get_username_field(self):
        return self.is_visible(self.USERNAME)
        
    def get_password_field(self):
        return self.is_visible(self.PASSWORD)
        
    def get_login_button(self):
        return self.is_visible(self.LOGIN_BUTTON)