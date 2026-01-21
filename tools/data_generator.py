from faker import Faker


class DataGenerator:
    def __init__(self, faker: Faker):
        self.faker = faker

    def first_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def email(self) -> str:
        return self.faker.email()

    def password(self) -> str:
        return self.faker.password()


fake_ru = DataGenerator(faker=Faker('ru_RU'))
