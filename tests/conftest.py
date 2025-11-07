from typing import Callable

import pytest
from playwright.sync_api import sync_playwright, ViewportSize

from constants import MAIN_PAGE_URL, SCREEN_WIDTH, SCREEN_HEIGHT, LOGIN_PAGE_URL, STAGE_BUILDER_PAGE
from src.elements.header import Header
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.pages.stage_builder_page import StageBuilderPage


# playwright
@pytest.fixture
def create_playwright():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture
def chrome_browser(create_playwright):
    browser = create_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def chrome_page(chrome_browser):
    context = chrome_browser.new_context(viewport=ViewportSize(width=SCREEN_WIDTH, height=SCREEN_HEIGHT))
    page = context.new_page()
    yield page
    page.close()
    context.close()


# pages
@pytest.fixture
def page_object(chrome_page) -> Callable:
    def _page(page_url, page_class, is_open):
        if is_open:
            chrome_page.goto(page_url, wait_until='load')
        return page_class(chrome_page)
    return _page


@pytest.fixture
def main_page(chrome_page, page_object) -> Callable:
    def _page(is_open: bool = True) -> MainPage:
        return page_object(MAIN_PAGE_URL, MainPage, is_open)
    return _page


@pytest.fixture
def login_page(chrome_page, page_object) -> Callable:
    def _page(is_open: bool = True) -> LoginPage:
        return page_object(LOGIN_PAGE_URL, LoginPage, is_open)
    return _page


@pytest.fixture
def stage_builder_page(chrome_page, page_object) -> Callable:
    def _page(is_open: bool = True) -> StageBuilderPage:
        return page_object(STAGE_BUILDER_PAGE, StageBuilderPage, is_open)
    return _page


# elements
@pytest.fixture
def header(chrome_page):
    return Header(chrome_page)


# post-actions
@pytest.fixture
def logout_after_test(header):
    yield
    header.logout()
