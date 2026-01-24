from playwright.sync_api import Page


class BaseElement:
    """
    Базовый элемент
    """

    def __init__(self, page: Page):
        self.page = page
