from playwright.sync_api import Page

from components.block_components.home_page.category_block import CategoryBlock
from components.block_components.home_page.futured_products_block import FeaturedProductsBlock
from components.block_components.home_page.news_block import NewsBlock
from components.block_components.home_page.poll_block import PollBlock
from components.block_components.home_page.welcome_block import WelcomeBlock
from components.footer import Footer
from components.header import Header
from components.success_bar import SuccessBar
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.header = Header(self.page)

        self.success_bar = SuccessBar(self.page)

        self.welcome_block = WelcomeBlock(self.page)
        self.category_block = CategoryBlock(self.page)
        self.featured_products_block = FeaturedProductsBlock(self.page)
        self.news_block = NewsBlock(self.page)
        self.poll_block = PollBlock(self.page)

        self.footer = Footer(self.page)

    def check_visibility(self):
        self.welcome_block.check_visibility()
        self.category_block.check_visibility()
        self.featured_products_block.check_visibility()
        self.news_block.check_visibility()
        self.poll_block.check_visibility()
