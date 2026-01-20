from playwright.sync_api import Page, expect

from components.header import Header
from components.login_form import LoginForm
from pages.base_page import BasePage
from components.footer import Footer


class LoginPage(BasePage):
    """
    Страница логина

    Описывает локаторы и методы взаимодействия со страницей
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.header = Header(self.page)
        self.login_form_title = self.page.locator("div.page-title h1")
        self.login_form = LoginForm(self.page)
        self.registration_button = self.page.locator("button.register-button")
        self.login_button = self.page.locator("button.login-button")
        self.authorization_info_title = self.page.locator("div.topic-block h2")
        self.authorization_info_text = self.page.locator("div.topic-block p")
        self.footer = Footer(self.page)

    def check_visibility(self) -> None:
        self.header.check_visibility()
        expect(self.login_form_title).to_be_visible()
        self.login_form.check_visibility()
        expect(self.registration_button).to_be_visible()
        expect(self.login_button).to_be_visible()
        expect(self.authorization_info_title).to_be_visible()
        expect(self.authorization_info_text).to_be_visible()
        self.footer.check_visibility()

    def click_registration_button(self) -> None:
        expect(self.registration_button).to_be_enabled()
        self.registration_button.click()

    def click_login_button(self) -> None:
        expect(self.login_button).to_be_enabled()
        self.login_button.click()


