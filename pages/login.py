from playwright.sync_api import Page, expect

from components.footer import Footer
from components.form_components.login_form import LoginForm
from components.header import Header
from pages.base_page import BasePage


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
        self.authorization_info_title = self.page.locator("div.topic-block h2")
        self.authorization_info_text = self.page.locator("div.topic-block p")

        self.footer = Footer(self.page)

    def check_visibility(self) -> None:
        expect(self.login_form_title).to_be_visible()
        self.login_form.check_visibility()
        expect(self.authorization_info_title).to_be_visible()
        expect(self.authorization_info_text).to_be_visible()


