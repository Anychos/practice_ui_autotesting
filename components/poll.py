from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class Poll(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.root = self.page.locator("div.poll")
        self.title = self.root.locator("strong").first
        self.answer_text = self.root.locator("label").first
        self.answer_radio_button = self.page.locator("input").first
        self.vote_button = self.root.locator("button")

        self.error_message = self.root.locator("div.poll-vote-error")

    def check_visibility(self):
        expect(self.title).to_be_visible()
        expect(self.answer_text).to_be_visible()
        expect(self.answer_radio_button).to_be_visible()
        expect(self.vote_button).to_be_visible()

    def click_answer(self):
        expect(self.answer_radio_button).to_be_visible()
        self.answer_radio_button.check()
        expect(self.answer_radio_button).to_be_checked()

    def click_vote_button(self):
        expect(self.vote_button).to_be_enabled()
        self.vote_button.click()

    def check_error_message(self):
        expect(self.error_message).to_be_visible()
