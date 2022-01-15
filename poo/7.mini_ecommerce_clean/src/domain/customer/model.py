from datetime import date
from src.domain.address.model import Address


class Customer:
    def __init__(self, first_name: str, last_name: str, phone_number: str, genre: str, document_id: str, birth_date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.genre = genre
        self.document_id = document_id
        self.birth_date = birth_date
        self.addresses = []

    def add_address(self, address: Address):
        # print(self.first_name)
        primary_address = list(
            filter(lambda ad: ad.primary == True, self.addresses)
        )

        # print(primary_address)

        if len(primary_address) > 0:
            self.addresses[-1].primary = False
            address.primary = True  # COMPORTAMENTO ESTRANHO

        self.addresses.append(address)
        # print(list(f"{x.address} {x.primary}" for x in self.addresses))
