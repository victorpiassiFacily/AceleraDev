from pydantic import BaseModel


class AddressSchema(BaseModel):
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: str
    customer_id: str


class ShowAddressSchema(AddressSchema):
    id: int

    class Config:
        orm_mode = True
