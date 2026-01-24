import pytest

from pages.home import MainPage
from tools.routes import Routes


@pytest.mark.header
@pytest.mark.regression
class TestHeader:
    def test_header_visibility_unauthorized_user(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.header.check_visibility()

    def test_navigation_links_redirect_to_correct_pages(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.header.click_navigation_link("register")
        main_page.check_current_url(Routes.REGISTRATION)

        main_page.header.click_navigation_link("login")
        main_page.check_current_url(Routes.LOGIN)

        main_page.header.click_navigation_link("wishlist")
        main_page.check_current_url(Routes.WISHLIST)

        main_page.header.click_navigation_link("cart")
        main_page.check_current_url(Routes.CART)

    def test_category_link_redirect_to_correct_page(self, main_page: MainPage) -> None: # Можно дополнить тест проверками всех ссылок исходя из критичности для бизнеса
        main_page.open_page(Routes.HOME)

        category_href = main_page.header.get_href(main_page.header.category_link)
        main_page.header.click_category_link()
        main_page.check_current_url(category_href)

    def test_search_product_button_redirect_to_search_result(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.header.fill_search_field("phone")
        main_page.header.click_search_button()
        main_page.check_current_url("/search?q=phone")

    def test_shop_logo_redirect_from_register_page(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.header.click_navigation_link("register")
        main_page.check_current_url(Routes.REGISTRATION)
        main_page.header.click_shop_logo()
        main_page.check_current_url(Routes.HOME)
