from playwright.sync_api import Page, expect, Locator

from components.base_component import BaseComponent


class Footer(BaseComponent):
    """
    Компонент футера

    Описывает локаторы и методы взаимодействия с футером
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.follow_us_block = self.page.locator("div.social")
        self.follow_us_title = self.follow_us_block.locator("h2")
        self.follow_us_link = self.follow_us_block.locator("a").first

        self.newsletter_block = self.page.locator("div.newsletter")
        self.newsletter_title = self.newsletter_block.locator("h2")
        self.email_input = self.page.locator("input#newsletter-email")
        self.subscribe_button = self.page.locator("button#newsletter-subscribe-button")

        self.powered_by_text = self.page.locator("div.footer-powered-by")
        self.copyright_text = self.page.locator("span.footer-disclaimer")

    def navigation_menu_title(self, index: int) -> Locator:
        return self.page.locator("h2.footer-menu__title").nth(index)

    def menu_links_container(self, index: int) -> Locator:
        return self.page.locator("div.footer-menu__list").nth(index)

    def menu_link(self, index: int) -> Locator:
        return self.menu_links_container(index).locator("a.footer-menu__link").first

    def check_visibility(self):
        expect(self.navigation_menu_title(0)).to_be_visible()
        expect(self.menu_link(0)).to_be_visible()

        expect(self.navigation_menu_title(1)).to_be_visible()
        expect(self.menu_link(1)).to_be_visible()

        expect(self.navigation_menu_title(2)).to_be_visible()
        expect(self.menu_link(2)).to_be_visible()

        expect(self.follow_us_title).to_be_visible()
        expect(self.follow_us_link).to_be_visible()

        expect(self.newsletter_title).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.subscribe_button).to_be_visible()

        expect(self.powered_by_text).to_be_visible()
        expect(self.copyright_text).to_be_visible()

    def click_menu_link(self, index: int):
        expect(self.menu_link(index)).to_be_visible()
        self.menu_link(index).click()

    def click_social_link(self):
        expect(self.follow_us_link).to_be_visible()
        self.follow_us_link.click()

    def fill_newsletter_email(self, email: str):
        expect(self.email_input).to_be_editable()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

    def click_subscribe_button(self):
        expect(self.subscribe_button).to_be_visible()
        self.subscribe_button.click()
