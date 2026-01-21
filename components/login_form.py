from playwright.sync_api import Page, expect, Locator
from pydantic import EmailStr

from components.base_component import BaseComponent


class LoginForm(BaseComponent):
    """
    Компонент формы логина

    Описывает локаторы и методы взаимодействия с формой
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.new_customer_text = self.page.locator("div.text")
        self.remember_me_checkbox = self.page.locator("input#RememberMe")
        self.forgot_password_link = self.page.locator("span.forgot-password")
        self.password_show_icon = self.page.locator("span.password-eye")
        self.password_hide_icon = self.page.locator("span.password-eye-open")

    def fieldset_title(self, index: int) -> Locator:
        return self.page.locator("div.customer-blocks h2.title").nth(index)

    def input_name(self, label: str) -> Locator:
        return self.page.locator(f"label[for={label}]")

    def input(self, element_id: str) -> Locator:
        return self.page.locator(f"input#{element_id}")

    def check_visibility(self) -> None:
        expect(self.fieldset_title(0)).to_be_visible()

        expect(self.new_customer_text).to_be_visible()

        expect(self.fieldset_title(1)).to_be_visible()

        expect(self.input_name("Email")).to_be_visible()
        expect(self.input("Email")).to_be_visible()
        expect(self.input_name("Password")).to_be_visible()
        expect(self.input("Password")).to_be_visible()
        expect(self.password_show_icon).to_be_visible()

        expect(self.remember_me_checkbox).to_be_visible()
        expect(self.input_name("RememberMe")).to_be_visible()
        expect(self.forgot_password_link).to_be_visible()

    def fill_form(self,
                  *,
                  email: EmailStr,
                  password: str,
                  remember_me: bool = False
                  ) -> None:
        """
        Заполняет форму логина

        :param email: Email пользователя
        :param password: Пароль пользователя
        :param remember_me: Флаг - нужно ли запомнить пользователя
        """

        expect(self.input("Email")).to_be_editable()
        self.input("Email").fill(email)
        expect(self.input("Email")).to_have_value(email)

        expect(self.input("Password")).to_be_editable()
        self.input("Password").fill(password)
        self.password_show_icon.click()
        expect(self.password_hide_icon).to_be_visible()
        expect(self.input("Password")).to_have_value(password)

        if remember_me:
            expect(self.remember_me_checkbox).to_be_visible()
            self.remember_me_checkbox.check()
            expect(self.remember_me_checkbox).to_be_checked()

    def click_show_password(self) -> None:
        expect(self.password_show_icon).to_be_visible()
        self.password_show_icon.click()
        expect(self.password_hide_icon).to_be_visible()

    def click_hide_password(self) -> None:
        expect(self.password_hide_icon).to_be_visible()
        self.password_hide_icon.click()
        expect(self.password_show_icon).to_be_visible()

    def click_forgot_password(self) -> None:
        expect(self.forgot_password_link).to_be_visible()
        self.forgot_password_link.click()

