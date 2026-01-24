from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.poll import Poll


class PollBlock(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.root = self.page.locator("section.home-page-polls")
        self.title = self.root.locator("h2.title")
        self.poll = Poll(self.page)

    def check_visibility(self):
        expect(self.title).to_be_visible()
        self.poll.check_visibility()
