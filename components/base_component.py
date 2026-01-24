from typing import Optional

from playwright.sync_api import Page, Locator


class BaseComponent:
    """
    Базовый компонент
    """

    def __init__(self, page: Page):
        self.page = page

    def get_href(self,
                 locator: Optional[Locator] = None,
                 selector: Optional[str] = None
                 ) -> str:
        """
        Получает значение атрибута href у элемента

        Можно передать либо готовый локатор, либо селектор для поиска
        """

        if locator:
            element = locator
        else:
            element = self.page.locator(selector)

        return element.get_attribute("href")
