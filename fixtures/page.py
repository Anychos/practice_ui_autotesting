import pytest
from playwright.sync_api import Page

from pages.login import LoginPage
from pages.main import MainPage
from pages.registartion import RegistrationPage


@pytest.fixture
def registration_page(open_chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(open_chromium_page)

@pytest.fixture
def login_page(open_chromium_page: Page) -> LoginPage:
    return LoginPage(open_chromium_page)

@pytest.fixture
def main_page(open_chromium_page: Page) -> MainPage:
    return MainPage(open_chromium_page)
