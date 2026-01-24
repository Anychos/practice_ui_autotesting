import pytest

from fixtures.user import UserData
from pages.login import LoginPage
from pages.registartion import RegistrationPage
from tools.routes import Routes


@pytest.mark.login
@pytest.mark.regression
class TestLogin:
    def test_login_page_visibility(self, login_page: LoginPage) -> None:
        login_page.open_page(Routes.LOGIN)

        login_page.check_visibility()

    @pytest.mark.e2e
    def test_successful_registration_logout_login(self,
                                                  registration_page: RegistrationPage,
                                                  login_page: LoginPage,
                                                  user_data_function: UserData
                                                  ) -> None:
        registration_page.open_page(Routes.REGISTRATION)

        registration_page.registration_form.fill_form(
            first_name=user_data_function.first_name,
            last_name=user_data_function.last_name,
            email=user_data_function.email,
            password=user_data_function.password
        )
        registration_page.registration_form.click_registration_button()
        registration_page.check_success_message()
        registration_page.header.check_visibility(is_logged_in=True)

        registration_page.header.click_navigation_link("logout")
        registration_page.header.check_visibility()

        registration_page.header.navigation_link("login").click()
        login_page.login_form.fill_form(
            email=user_data_function.email,
            password=user_data_function.password
        )
        login_page.login_form.click_login_button()
        registration_page.header.check_visibility(is_logged_in=True)

