from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс страницы браузера

    Описывает общие методы работы со страницами
    """

    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def reload_page(self) -> None:
        self.page.reload()
