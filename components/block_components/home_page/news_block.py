from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.card_components.news_card import NewsCard


class NewsBlock(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.root = self.page.locator("section.news-list-homepage")
        self.title = self.root.locator("h2.title")
        self.news_card = NewsCard(self.page)
        self.news_archive_link = self.root.locator("div.view-all a")

    def check_visibility(self):
        expect(self.title).to_be_visible()
        self.news_card.check_visibility()
        expect(self.news_archive_link).to_be_visible()

    def click_news_archive_link(self):
        expect(self.news_archive_link).to_be_visible()
        self.news_archive_link.click()
