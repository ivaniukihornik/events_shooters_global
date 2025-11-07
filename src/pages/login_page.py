from playwright.sync_api import Page

from constants import USER_PASSWORD, USER_EMAIL
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_or_phone_field = self.page.locator('input[name=emailOrPhoneNumber]')
        self.password_field = self.page.locator('input[name=password]')
        self.submit_button = self.page.locator('button[type=submit]')

    def login(self, email_or_phone: str = USER_EMAIL, password: str = USER_PASSWORD) -> None:
        self.email_or_phone_field.type(email_or_phone)
        self.password_field.type(password)
        self.submit_button.click()
