from pages.registartion import RegistrationPage
from tools.data_generator import fake_ru
from tools.routes import Routes


class TestRegistration:
    def test_check_registration_page_visibility(self, registration_page: RegistrationPage) -> None:
        registration_page.open_page(Routes.REGISTRATION)
        registration_page.check_visibility()

    def test_successful_registration(self, registration_page: RegistrationPage) -> None:
        registration_page.open_page(Routes.REGISTRATION)
        registration_page.registration_form.fill_form(
            first_name=fake_ru.first_name(),
            last_name=fake_ru.last_name(),
            email=fake_ru.email(),
            password=fake_ru.password()
        )
        registration_page.click_registration_button()
        registration_page.check_success_message()
        registration_page.click_continue_button()

    def test_successful_registration_with_gender(self, registration_page: RegistrationPage) -> None:
        registration_page.open_page(Routes.REGISTRATION)
        registration_page.registration_form.fill_form(
            first_name=fake_ru.first_name(),
            last_name=fake_ru.last_name(),
            email=fake_ru.email(),
            password=fake_ru.password(),
            is_gender=True
        )
        registration_page.click_registration_button()
        registration_page.check_success_message()
        registration_page.click_continue_button()
