from playwright.sync_api import Page, expect

from components.header import Header
from pages.base_page import BasePage
from components.registration_form import RegistrationForm
from components.footer import Footer


class RegistrationPage(BasePage):
    """
    Страница регистрации

    Описывает локаторы и методы взаимодействия со страницей
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.header = Header(self.page)
        self.registration_form_title = self.page.locator("div.page-title h1")
        self.registration_form = RegistrationForm(self.page)
        self.registration_button = self.page.locator("button#register-button")
        self.success_message = self.page.locator("div.result")
        self.continue_button = self.page.locator("a.register-continue-button")
        self.footer = Footer(self.page)

    def check_visibility(self) -> None:
        self.header.check_visibility()
        expect(self.registration_form_title).to_be_visible()
        self.registration_form.check_visibility()
        expect(self.registration_button).to_be_visible()
        self.footer.check_visibility()

    def click_registration_button(self) -> None:
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def check_success_message(self) -> None:
        expect(self.success_message).to_be_visible()
        expect(self.continue_button).to_be_visible()

    def click_continue_button(self) -> None:
        expect(self.continue_button).to_be_enabled()
        self.continue_button.click()
