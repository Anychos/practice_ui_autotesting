from playwright.sync_api import Page, expect


class BasePage:
    """
    Базовый класс страницы браузера

    Описывает общие методы работы со страницами
    """

    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def reload_page(self) -> None:
        self.page.reload()

    def check_current_url(self, expected_url: str) -> None:
        expect(self.page).to_have_url(expected_url)
