from playwright.sync_api import Page, Locator, expect

from components.base_component import BaseComponent


class CategoryCard(BaseComponent):
    """
    Компонент карточки категории товаров на главной странице
    """

    def __init__(self, page: Page, index: int = 0):
        super().__init__(page)

        self.root = page.locator("article.item-box").nth(index)
        self.title = self.root.locator("h2")
        self.image = self.root.locator("div.picture")

    def check_visibility(self) -> None:
        expect(self.title).to_be_visible()
        expect(self.image).to_be_visible()

    def click_card(self) -> None:
        expect(self.root).to_be_visible()
        self.root.click()
