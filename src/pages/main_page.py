from playwright.sync_api import Page

from constants import MINIMAL_WAITING_TIMEOUT_MS
from src.base_page import BasePage
from src.pages.login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.build_for_free_button = page.locator('//main//button[text()="Build for free"]')

    def click_build_for_free_button(self, is_user_logged_in: bool) -> 'LoginPage':
        login_page = LoginPage(self.page)
        self.poll_click(
            locator=self.build_for_free_button,
            playwright_wait=lambda: login_page.email_or_phone_field.wait_for(
                state='visible',
                timeout=MINIMAL_WAITING_TIMEOUT_MS
            )
        )
        return login_page
