from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class Poll(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = self.page.locator("strong.poll-display-text").first
        self.answer_text = self.page.locator("ul.poll-options label").first
        self.answer_radio_button = self.page.locator("ul.poll-options input").first

    def check_visibility(self):
        expect(self.title).to_be_visible()
        expect(self.answer_text).to_be_visible()
        expect(self.answer_radio_button).to_be_visible()

    def click_answer(self):
        expect(self.answer_radio_button).to_be_visible()
        self.answer_radio_button.check()
        expect(self.answer_radio_button).to_be_checked()
