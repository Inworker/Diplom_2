from faker import Faker

fake = Faker()


class CreateCurrierData:
    @staticmethod
    def generate_currier_data():
        CREATE_COURIER_BODY = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return CREATE_COURIER_BODY

    @staticmethod
    def generate_fake_user_data():
        CREATE_COURIER_BODY = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.first_name()
        }
        return CREATE_COURIER_BODY

    @staticmethod
    def generate_fake_email():
        FAKE_EMAIL = {"email": fake.email()}
        return FAKE_EMAIL

    FIRST_INGREDIENT = {"ingredients": "61c0c5a71d1f82001bdaaa6d"}
    BAD_INGREDIENT = {"ingredients": "01bdaaa6d"}
    SECOND_INGREDIENT = {"ingredients": "61c0c5a71d1f82001bdaaa6f"}