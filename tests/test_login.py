from pages.login import LoginPage
from pages.registartion import RegistrationPage
from tools.data_generator import fake_ru
from tools.routes import Routes


class TestLogin:
    def test_login_page_visibility(self, login_page: LoginPage) -> None:
        login_page.open_page(Routes.LOGIN)
        login_page.check_visibility()

    def test_successful_login(self,
                              registration_page: RegistrationPage,
                              login_page: LoginPage
                              ) -> None:
        first_name = fake_ru.first_name()
        last_name = fake_ru.last_name()
        email = fake_ru.email()
        password = fake_ru.password()

        registration_page.open_page(Routes.REGISTRATION)
        registration_page.registration_form.fill_form(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        registration_page.click_registration_button()
        registration_page.header.click_navigation_link("logout")

        login_page.open_page(Routes.LOGIN)
        login_page.login_form.fill_form(
            email=email,
            password=password
        )
        login_page.click_login_button()
