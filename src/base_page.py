import time
from typing import Callable

from playwright.sync_api import Page, Locator, TimeoutError

from constants import SCREENSHOTS_DIR, DEFAULT_WAITING_TIMEOUT_MS, MINIMAL_WAITING_TIMEOUT_MS


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def browser_url(self):
        return self.page.evaluate('window.location.href')

    @staticmethod
    def poll_click(
            locator: Locator,
            playwright_wait: Callable,
            timeout_s: float = DEFAULT_WAITING_TIMEOUT_MS / 1000
    ) -> None:
        end_time = time.time() + timeout_s
        while time.time() < end_time:
            try:
                locator.click(timeout=MINIMAL_WAITING_TIMEOUT_MS)
                playwright_wait()
            except TimeoutError:
                pass
            else:
                return

        raise TimeoutError('Timeout expired! Predicate was not achieved!')

    def take_screenshot(self, screenshot_name: str) -> None:
        self.page.screenshot(path=f'{SCREENSHOTS_DIR}/{screenshot_name}.png', full_page=True)
        return None
