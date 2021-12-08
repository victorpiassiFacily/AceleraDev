from datetime import date
from pydantic import BaseModel


class UpdateCustomerSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    phone_number: str
    genre: str


class CustomerSchema(UpdateCustomerSchema):
    document_id: str


class ShowCustomerSchema(CustomerSchema):
    id: int

    class Config:
        orm_mode = True
