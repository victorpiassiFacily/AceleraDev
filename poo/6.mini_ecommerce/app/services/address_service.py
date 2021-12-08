from fastapi import Depends
from app.repositories.address_repository import AddressRepository
from app.api.address.schemas import AddressSchema


class AddressService:
    def __init__(
        self,
        address_repository: AddressRepository = Depends()
    ):
        self.address_repository = address_repository

    def check_primary_address(self, address: AddressSchema):
        if address.primary:
            primary_address = self.address_repository.get_customer_primary_address(
                address.customer_id)
            if primary_address:
                self.address_repository.upgrade(
                    primary_address.id, {"primary": False}
                )
