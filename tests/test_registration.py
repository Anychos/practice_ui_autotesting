import pytest

from fixtures.user import UserData
from pages.registartion import RegistrationPage
from tools.routes import Routes


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    def test_check_registration_page_visibility(self, registration_page: RegistrationPage) -> None:
        registration_page.open_page(Routes.REGISTRATION)

        registration_page.check_visibility()

    @pytest.mark.smoke
    def test_successful_registration(self,
                                     registration_page: RegistrationPage,
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
        registration_page.click_continue_button()
        registration_page.header.check_visibility(is_logged_in=True)

    def test_successful_registration_with_gender(self,
                                                 registration_page: RegistrationPage,
                                                 user_data_function: UserData
                                                 ) -> None:
        registration_page.open_page(Routes.REGISTRATION)

        registration_page.registration_form.fill_form(
            first_name=user_data_function.first_name,
            last_name=user_data_function.last_name,
            email=user_data_function.email,
            password=user_data_function.password,
            is_gender=True
        )
        registration_page.registration_form.click_registration_button()
        registration_page.check_success_message()
        registration_page.click_continue_button()
        registration_page.header.check_visibility(is_logged_in=True)
