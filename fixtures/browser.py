import pytest
from playwright.sync_api import Page, Playwright

from config import settings
from pages.registartion import RegistrationPage
from tools.routes import Routes


@pytest.fixture
def open_chromium_page(playwright: Playwright) -> Page:
    """
    Запускает Chromium браузер и открывает страницу приложения

    :param playwright: Экземпляр Playwright, предоставляемый pytest-playwright
    :return: Объект Page для взаимодействия со страницей
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="session")
def get_browser_state(playwright: Playwright) -> None:
    """
    Запускает Chromium браузер, создает и сохраняет состояние браузера зарегистрированного пользователя

    :param playwright: Экземпляр Playwright, предоставляемый pytest-playwright
    :return: Файл с состоянием браузера
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.open_page(Routes.REGISTRATION)
    registration_page.registration_form.fill_form(
        first_name=settings.test_user.first_name,
        last_name=settings.test_user.last_name,
        email=settings.test_user.email,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)

    context.close()
    browser.close()


@pytest.fixture
def open_chromium_page_with_state(playwright: Playwright) -> Page:
    """
    Запускает Chromium браузер и открывает страницу приложения с сохраненным состоянием

    :param playwright: Экземпляр Playwright, предоставляемый pytest-playwright
    :return: Объект Page для взаимодействия со страницей
    """

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=settings.browser_state_file
    )
    page = context.new_page()
    yield page
    context.close()
    browser.close()


