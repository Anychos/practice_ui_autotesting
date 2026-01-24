from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class WelcomeBlock(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.promo_slider = self.page.locator("div.swiper")
        self.title = self.page.locator("div.topic-block-title")
        self.text = self.page.locator("div.topic-block-body")

    def check_visibility(self):
        expect(self.promo_slider).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.text).to_be_visible()

    def click_promo_slider(self):
        expect(self.promo_slider).to_be_visible()
        self.promo_slider.click()
