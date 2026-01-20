from playwright.sync_api import Page, expect, Locator
from components.base_component import BaseComponent


class Header(BaseComponent):
    """
    Компонент хедера

    Описывает локаторы и методы взаимодействия с хедером
    """

    def __init__(self, page: Page):
        super().__init__(page)

        self.shop_logo = self.page.locator("div.header-logo")
        self.search_field = self.page.locator("input.search-box-text")
        self.search_button = self.page.locator("button.search-box-button")
        self.category_link = self.page.locator("a.menu__link").first

    def navigation_link(self, link_name: str) -> Locator:
        return self.page.locator(f"a.ico-{link_name}")

    def navigation_link_quantity_counter(self, link_name: str) -> Locator:
        return self.page.locator(f"span.{link_name}-qty")

    def check_visibility(self,
                         *,
                         is_logged_in: bool = False
                         ) -> None:
        """
        Проверяет видимость элементов в форме

        :param is_logged_in: Флаг - залогинен ли пользователь или нет
        """

        if is_logged_in:
            expect(self.navigation_link("account")).to_be_visible()
            expect(self.navigation_link("logout")).to_be_visible()
        else:
            expect(self.navigation_link("register")).to_be_visible()
            expect(self.navigation_link("login")).to_be_visible()
        expect(self.navigation_link("wishlist")).to_be_visible()
        expect(self.navigation_link("cart")).to_be_visible()

        expect(self.shop_logo).to_be_visible()
        expect(self.search_field).to_be_visible()
        expect(self.search_button).to_be_visible()

        expect(self.category_link).to_be_visible()

    def click_navigation_link(self, name: str) -> None:
        expect(self.navigation_link(name)).to_be_visible()
        self.navigation_link(name).click()

    def click_shop_logo(self) -> None:
        expect(self.shop_logo).to_be_visible()
        self.shop_logo.click()

    def fill_search_field(self, text: str) -> None:
        expect(self.search_field).to_be_editable()
        self.search_field.fill(text)
        expect(self.search_field).to_have_value(text)

    def click_search_button(self) -> None:
        expect(self.search_button).to_be_enabled()
        self.search_button.click()

    def click_category_link(self) -> None:
        expect(self.category_link).to_be_visible()
        self.category_link.click()


