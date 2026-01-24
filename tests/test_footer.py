import pytest
from playwright.sync_api import expect

from pages.home import MainPage
from tools.data_generator import fake_ru
from tools.routes import Routes


@pytest.mark.footer
@pytest.mark.regression
class TestFooter:
    def test_footer_visibility(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.footer.check_visibility()

    def test_footer_menu_link_redirect_to_correct_page(self, main_page: MainPage) -> None: # Можно дополнить тест проверками всех ссылок исходя из критичности для бизнеса
        main_page.open_page(Routes.HOME)

        link_href = main_page.footer.get_href(main_page.footer.menu_link(0))
        main_page.footer.click_menu_link(0)
        main_page.check_current_url(link_href)

    @pytest.mark.skip(reason="все ссылки работают только с впн")
    def test_footer_social_link_redirect_to_correct_page(self, main_page: MainPage) -> None:  # Можно дополнить тест проверками всех ссылок исходя из критичности для бизнеса
        main_page.open_page(Routes.HOME)

        social_link_href = main_page.footer.get_href(main_page.footer.follow_us_link)
        with main_page.page.expect_popup() as popup_info:
            main_page.footer.click_social_link()

        new_page = popup_info.value
        new_page.wait_for_load_state("domcontentloaded")
        expect(new_page).to_have_url(social_link_href)

    def test_subscribe_to_newsletter(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.footer.fill_newsletter_email(fake_ru.email())
        main_page.footer.click_subscribe_button()
        main_page.footer.check_subscribe_success_message()


