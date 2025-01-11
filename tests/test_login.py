import pytest
from pages.login_page import LoginPage
from config.config import TestData

class TestLogin:
    def test_fields(self, init_driver):
        self.login_page = LoginPage(init_driver)
        assert self.login_page.get_username_field(), "Username field selector was not found on page"
        assert self.login_page.get_password_field(), "Password field selector was not found on page"
        assert self.login_page.get_login_button(), "Login button selector was not found on page"
        

    def test_login_success(self, init_driver):
        self.login_page = LoginPage(init_driver)

        self.login_page.login(TestData.USERNAME, TestData.PASSWORD)
        assert self.login_page.get_cart_icon(), "Profile picture selector was not found on page"
        