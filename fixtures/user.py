import pytest
from pydantic import BaseModel, EmailStr

from tools.data_generator import fake_ru


class UserData(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


@pytest.fixture
def user_data_function() -> UserData:
    return UserData(
        first_name=fake_ru.first_name(),
        last_name=fake_ru.last_name(),
        email=fake_ru.email(),
        password=fake_ru.password()
    )


