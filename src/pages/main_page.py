from playwright.sync_api import Page

from constants import LOGIN_PAGE_URL_GET_STARTED
from src.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.build_for_free_button = page.locator('//main//button[text()="Build for free"]')

    def click_build_for_free_button(self, is_user_logged_in: bool) -> None:
        self.poll_click(
            locator=self.build_for_free_button,
            predicate=lambda: self.browser_url == LOGIN_PAGE_URL_GET_STARTED
        )
