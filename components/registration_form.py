from playwright.sync_api import Page, expect, Locator
from pydantic import EmailStr

from components.base_component import BaseComponent


class RegistrationForm(BaseComponent):
    """
    Компонент формы регистрации

    Описывает локаторы и методы взаимодействия с формой
    """

    def __init__(self, page: Page):
        super().__init__(page)

    def fieldset_title(self, index: int) -> Locator:
        return self.page.locator("section.fieldset h2.title").nth(index)

    def input_name(self, label: str) -> Locator:
        return self.page.locator(f"label[for={label}]")

    def input(self, element_id: str) -> Locator:
        return self.page.locator(f"input#{element_id}")

    def radio_button(self, element_id: str) -> Locator:
        return self.page.locator(f"input#{element_id}")

    def required_field_mark(self, index: int) -> Locator:
        return self.page.locator("span.required").nth(index)

    def check_visibility(self) -> None:
        expect(self.fieldset_title(0)).to_be_visible()

        expect(self.input_name("gender")).to_be_visible()
        expect(self.input_name("gender-male")).to_be_visible()
        expect(self.radio_button("gender-male")).to_be_visible()
        expect(self.input_name("gender-female")).to_be_visible()
        expect(self.radio_button("gender-female")).to_be_visible()

        expect(self.input_name("FirstName")).to_be_visible()
        expect(self.input("FirstName")).to_be_visible()
        expect(self.required_field_mark(0)).to_be_visible()

        expect(self.input_name("LastName")).to_be_visible()
        expect(self.input("LastName")).to_be_visible()
        expect(self.required_field_mark(1)).to_be_visible()

        expect(self.input_name("Email")).to_be_visible()
        expect(self.input("Email")).to_be_visible()
        expect(self.required_field_mark(2)).to_be_visible()

        expect(self.fieldset_title(1)).to_be_visible()

        expect(self.input_name("Password")).to_be_visible()
        expect(self.input("Password")).to_be_visible()
        expect(self.required_field_mark(3)).to_be_visible()

        expect(self.input_name("ConfirmPassword")).to_be_visible()
        expect(self.input("ConfirmPassword")).to_be_visible()
        expect(self.required_field_mark(4)).to_be_visible()

    def fill_form(self,
                  *,
                  first_name: str,
                  last_name: str,
                  email: EmailStr,
                  password: str,
                  is_gender: bool = False
                  ) -> None:
        """
        Заполняет форму регистрации

        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param email: Email пользователя
        :param password: Пароль пользователя
        :param is_gender: Флаг - нужно ли выбрать пол
        """

        expect(self.input("FirstName")).to_be_editable()
        self.input("FirstName").fill(first_name)
        expect(self.input("FirstName")).to_have_value(first_name)

        expect(self.input("LastName")).to_be_editable()
        self.input("LastName").fill(last_name)
        expect(self.input("LastName")).to_have_value(last_name)

        expect(self.input("Email")).to_be_editable()
        self.input("Email").fill(email)
        expect(self.input("Email")).to_have_value(email)

        expect(self.input("Password")).to_be_editable()
        self.input("Password").fill(password)

        expect(self.input("ConfirmPassword")).to_be_editable()
        self.input("ConfirmPassword").fill(password)

        if is_gender:
            expect(self.radio_button("gender-male")).to_be_visible()
            self.radio_button("gender-male").check()
            expect(self.radio_button("gender-male")).to_be_checked()
