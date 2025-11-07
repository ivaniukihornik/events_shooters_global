import time
from typing import Callable

from playwright.sync_api import Page, Locator, TimeoutError

from constants import DEFAULT_POLL_INTERVAL_S, SCREENSHOTS_DIR


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def browser_url(self):
        return self.page.evaluate('window.location.href')

    @staticmethod
    def poll_click(
            locator: Locator,
            predicate: Callable,
            timeout: int = DEFAULT_POLL_INTERVAL_S,
            poll_interval: float = DEFAULT_POLL_INTERVAL_S
    ) -> None:
        end_time = time.time() + timeout
        while time.time() < end_time:
            locator.click()
            try:
                predicate()
            except TimeoutError:
                time.sleep(poll_interval)
            else:
                return

        raise TimeoutError('Timeout expired! Predicate was not achieved!')

    def take_screenshot(self, screenshot_name: str) -> None:
        self.page.screenshot(path=f'{SCREENSHOTS_DIR}/{screenshot_name}.png', full_page=True)
        return None
