from playwright.sync_api import Page, TimeoutError

from constants import DEFAULT_WAITING_TIMEOUT_MS
from src.pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.avatar_label = self.page.locator('//div[contains(@class, "lg:flex")]//*[@aria-label="Account avatar"]')
        self.avatar_menu_button = self.page.locator('//div[contains(@class, "lg:flex")]'
                                                    '//*[@aria-label="Account avatar"]'
                                                    '/ancestor::button[@aria-haspopup="menu"]')
        self.logout_menu_button = self.page.locator('//*[@type="button"][text()="Log Out"]')
        self.logout_confirm_button = self.page.locator('//button[text()="Log Out"]')
        self.sign_in_button = self.page.locator('//button[normalize-space(.)="Sign in"]')

    def logout(self) -> None:
        if self.avatar_label.is_visible():
            self.avatar_menu_button.click()
            self.logout_menu_button.click()
            self.logout_confirm_button.click()
        try:
            self.sign_in_button.wait_for(state='visible', timeout=DEFAULT_WAITING_TIMEOUT_MS)
        except TimeoutError:
            raise Exception('Not logged out!')
        else:
            return
