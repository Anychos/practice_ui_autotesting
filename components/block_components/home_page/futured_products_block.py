from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.card_components.featured_product_card import FeaturedProductCard


class FeaturedProductsBlock(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.root = self.page.locator("section.home-page-product-grid")
        self.title = self.root.locator("h2.title")
        self.featured_product_card = FeaturedProductCard(self.page)

    def check_visibility(self):
        expect(self.title).to_be_visible()
        self.featured_product_card.check_visibility()
