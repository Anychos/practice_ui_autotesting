from pages.main import MainPage
from tools.routes import Routes


class TestMainPage:
    def test_main_page_visibility(self, main_page: MainPage) -> None:
        main_page.open_page(Routes.HOME)
        main_page.check_visibility()
