from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.card_components.category_card import CategoryCard


class CategoryBlock(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.root = self.page.locator("section.home-page-category-grid")
        self.category_card = CategoryCard(self.page)

    def check_visibility(self):
        self.category_card.check_visibility()

