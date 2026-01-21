from enum import Enum
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TEST_USER")

    first_name: str
    last_name: str
    email: EmailStr
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        return str(self.app_url)

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        browser_state_file = FilePath("browser-state.json")

        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()
