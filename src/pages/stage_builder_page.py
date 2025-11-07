import time

from playwright.sync_api import Page, TimeoutError, Position

from constants import DEFAULT_WAITING_TIMEOUT_MS, BUILDER_LOADING_TIMEOUT_MS
from src.base_page import BasePage


class StageBuilderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.limited_tablet_alert = self.page.locator('*[role=alertdialog]')
        self.limited_tablet_alert_confirm_button = self.page.locator('div[role=alertdialog] button')
        self.loading_screen = self.page.locator('section[id=unity-loading-screen]')
        self.builder_screen = self.page.locator('#unity-app-root')
        self.builder_canvas = self.page.frame_locator('#unity-app-root iframe').locator('canvas[id=unity-app-canvas]')
        self.DEFAULT_ONBOARDING_ALERT_CLOSE_BUTTON_X = 1344
        self.DEFAULT_ONBOARDING_ALERT_CLOSE_BUTTON_Y = 146
        self.ACTUAL_CANVAS_WIDTH = None
        self.ACTUAL_CANVAS_HEIGHT = None

    def confirm_limited_tablet_alert(self) -> 'StageBuilderPage':
        try:
            self.limited_tablet_alert.wait_for(state='visible', timeout=DEFAULT_WAITING_TIMEOUT_MS)
        except TimeoutError:
            return self
        else:
            self.limited_tablet_alert_confirm_button.click()

        return self

    def wait_for_loading_screen(self) -> 'StageBuilderPage':
        self.loading_screen.wait_for(state='visible')
        return self

    def wait_for_loading_screen_to_be_finished(self) -> 'StageBuilderPage':
        self.loading_screen.wait_for(state='hidden', timeout=BUILDER_LOADING_TIMEOUT_MS)
        return self

    def write_canvas_size(self) -> None:
        self.ACTUAL_CANVAS_WIDTH = int(self.builder_canvas.get_attribute('width'))
        self.ACTUAL_CANVAS_HEIGHT = int(self.builder_canvas.get_attribute('height'))

    def close_onboarding_alert(self) -> 'StageBuilderPage':
        time.sleep(3)  # НЕ ХОТІВ, ЗАСТАВИЛИ ((((
        if self.ACTUAL_CANVAS_WIDTH is None or self.ACTUAL_CANVAS_HEIGHT is None:
            self.write_canvas_size()
        self.builder_canvas.click(position=Position(
            x=self.DEFAULT_ONBOARDING_ALERT_CLOSE_BUTTON_X,
            y=self.DEFAULT_ONBOARDING_ALERT_CLOSE_BUTTON_Y
        ))
        self.take_screenshot('builder_canvas')
        return self
