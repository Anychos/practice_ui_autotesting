from playwright.sync_api import Page, expect

from components.card_components.category_card import CategoryCard
from components.card_components.featured_product_card import FeaturedProductCard
from components.card_components.news_card import NewsCard
from components.footer import Footer
from components.header import Header
from components.poll import Poll
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.header = Header(self.page)

        self.promo_slider = self.page.locator("div.swiper")
        self.welcome_title = self.page.locator("div.topic-block-title")
        self.welcome_text = self.page.locator("div.topic-block-body")

        self.category_block = self.page.locator("section.home-page-category-grid")
        self.category_card = CategoryCard(self.page)

        self.featured_products_block = self.page.locator("section.home-page-product-grid")
        self.featured_products_block_title = self.featured_products_block.locator("h2.title")
        self.featured_product_card = FeaturedProductCard(self.page)

        self.news_block = self.page.locator("section.news-list-homepage")
        self.news_block_title = self.news_block.locator("h2.title")
        self.news_card = NewsCard(self.page)
        self.view_news_archive_link = self.news_block.locator("div.view-all")

        self.poll_block = self.page.locator("section.home-page-polls")
        self.poll_block_title = self.poll_block.locator("h2.title")
        self.poll = Poll(self.page)
        self.vote_button = self.poll_block.locator("button.vote-poll-button")

        self.footer = Footer(self.page)

    def check_visibility(self):
        self.header.check_visibility()

        expect(self.promo_slider).to_be_visible()

        expect(self.welcome_title).to_be_visible()
        expect(self.welcome_text).to_be_visible()

        expect(self.category_block).to_be_visible()
        self.category_card.check_visibility()

        expect(self.featured_products_block).to_be_visible()
        expect(self.featured_products_block_title).to_be_visible()
        self.featured_product_card.check_visibility()

        expect(self.news_block).to_be_visible()
        expect(self.news_block_title).to_be_visible()
        self.news_card.check_visibility()
        expect(self.view_news_archive_link).to_be_visible()

        expect(self.poll_block).to_be_visible()
        expect(self.poll_block_title).to_be_visible()
        self.poll.check_visibility()
        expect(self.vote_button).to_be_visible()

        self.footer.check_visibility()
