from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SuccessBar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.success_bar = self.page.locator("div#bar-notification")
        self.success_bar_text = self.success_bar.locator("p.content")
        self.success_bar_text_link = self.success_bar_text.locator("a")
        self.success_bar_close_button = self.success_bar.locator("span.close")

    def check_visibility(self):
        expect(self.success_bar).to_be_visible()
        expect(self.success_bar_text).to_be_visible()
        expect(self.success_bar_close_button).to_be_visible()

    def click_close_button(self):
        expect(self.success_bar_close_button).to_be_visible()
        self.success_bar_close_button.click()
        expect(self.success_bar).not_to_be_visible()

    def click_text_link(self):
        expect(self.success_bar_text).to_be_visible()
        self.success_bar_text_link.click()


