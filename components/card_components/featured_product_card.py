from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class FeaturedProductCard(BaseComponent):
    """
    Компонент карточки рекомендуемого товара на главной странице
    """

    def __init__(self, page: Page, index: int = 2):
        super().__init__(page)

        self.root = page.locator("div.item-box").nth(index)
        self.image = self.root.locator("div.picture")
        self.image_href = self.image.locator("a")
        self.title = self.root.locator("h2 a")
        self.rating = self.root.locator("div.rating")
        self.actual_price = self.root.locator("span.actual-price")
        self.add_to_cart_button = self.root.locator("button.product-box-add-to-cart-button")
        self.add_to_wishlist_button = self.root.locator("button.add-to-wishlist-button")
        self.add_to_compare_button = self.root.locator("button.add-to-compare-list-button")

    def check_visibility(self) -> None:
        expect(self.image).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.rating).to_be_visible()
        expect(self.actual_price).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()
        expect(self.add_to_wishlist_button).to_be_visible()
        expect(self.add_to_compare_button).to_be_visible()

    def click_image(self) -> None:
        expect(self.image).to_be_visible()
        self.image.click()

    def click_title(self) -> None:
        expect(self.title).to_be_visible()
        self.title.click()

    def click_add_to_cart_button(self) -> None:
        expect(self.add_to_cart_button).to_be_enabled()
        self.add_to_cart_button.click()

    def click_add_to_wishlist_button(self) -> None:
        expect(self.add_to_wishlist_button).to_be_enabled()
        self.add_to_wishlist_button.click()

    def click_add_to_compare_button(self) -> None:
        expect(self.add_to_compare_button).to_be_enabled()
        self.add_to_compare_button.click()

