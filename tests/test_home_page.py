import pytest

from pages.home import MainPage
from tools.routes import Routes


@pytest.mark.main_page
@pytest.mark.regression
class TestHomePage:
    def test_home_page_visibility(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.check_visibility()

    def test_open_products_category(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        category_href = main_page.category_block.category_card.get_href(main_page.category_block.category_card.root_href)
        main_page.category_block.category_card.click_root_href()
        main_page.check_current_url(category_href)

    def test_open_featured_product_click_title(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        product_href = main_page.featured_products_block.featured_product_card.get_href(main_page.featured_products_block.featured_product_card.title)
        main_page.featured_products_block.featured_product_card.click_title()
        main_page.check_current_url(product_href)

    def test_open_featured_product_click_image(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        product_href = main_page.featured_products_block.featured_product_card.get_href(main_page.featured_products_block.featured_product_card.image_href)
        main_page.featured_products_block.featured_product_card.click_image()
        main_page.check_current_url(product_href)

    def test_add_featured_product_to_wishlist(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.featured_products_block.featured_product_card.click_add_to_wishlist_button()
        main_page.success_bar.check_visibility()

    def test_add_featured_product_to_cart(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.featured_products_block.featured_product_card.click_add_to_cart_button()
        main_page.success_bar.check_visibility()

    def test_add_featured_product_to_compare(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        main_page.featured_products_block.featured_product_card.click_add_to_compare_button()
        main_page.success_bar.check_visibility()

    def test_open_news_click_title(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        news_href = main_page.news_block.news_card.get_href(main_page.news_block.news_card.title_link)
        main_page.news_block.news_card.click_title()
        main_page.check_current_url(news_href)

    def test_open_news_click_details(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        news_href = main_page.news_block.news_card.get_href(main_page.news_block.news_card.details_button)
        main_page.news_block.news_card.click_details_button()
        main_page.check_current_url(news_href)

    def test_open_news_archive(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)

        archive_href = main_page.news_block.news_archive_link.get_attribute("href")
        main_page.news_block.click_news_archive_link()
        main_page.check_current_url(archive_href)
