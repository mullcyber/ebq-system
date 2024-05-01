from dataclasses import dataclass
from typing import Optional
import faker
from random import randint, choice
from data import PRODUCTS

fake = faker.Faker()


@dataclass
class Product:
    name: str
    amount: int


CONTACT_TYPE = ["email", "messenger", "sms"]


@dataclass
class Contact:
    type_: str
    value: Optional[str] = None

    def set_value(self) -> str:
        if self.type_ == "email":
            self.value = fake.email()
        elif self.type_ == "sms":
            self.value = fake.phone_number()
        else:
            self.value = "//:messenger-link"


@dataclass
class Request:
    fabric: str
    truck: str
    product: Product
    contact: Contact


def fake_request(amount: int):
    requests = []
    for _ in range(0, amount):
        product = Product(name=choice(PRODUCTS), amount=randint(10, 26))
        contact = Contact(type_=choice(CONTACT_TYPE))
        contact.set_value()
        request = Request(
            fabric=fake.company(),
            truck=fake.license_plate(),
            product=product.__dict__,
            contact=contact.__dict__,
        )
        requests.append(request.__dict__)
    return requests


if __name__ == "__main__":
    requests = fake_request(1)
    print("done")
