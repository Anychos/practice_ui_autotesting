from playwright.sync_api import Page, Locator, expect

from components.base_component import BaseComponent


class NewsCard(BaseComponent):
    """
    Компонент карточки новости на главной странице
    """

    def __init__(self, page: Page, index: int = 0):
        super().__init__(page)

        self.root = page.locator("article.news-item").nth(index)
        self.title = self.root.locator("h3")
        self.public_date = self.root.locator("time.news-date")
        self.text_preview = self.root.locator("section.news-body")
        self.details_button = self.root.locator("a.read-more")

    def check_visibility(self):
        expect(self.title).to_be_visible()
        expect(self.public_date).to_be_visible()
        expect(self.text_preview).to_be_visible()
        expect(self.details_button).to_be_visible()

    def click_title(self):
        expect(self.title).to_be_visible()
        self.title.click()

    def click_details_button(self):
        expect(self.details_button).to_be_visible()
        self.details_button.click()
