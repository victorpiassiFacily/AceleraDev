from datetime import date
from pydantic import BaseModel

from app.models.models import User


class UserSchema(BaseModel):
    display_name = str
    email = str
    password = str


class UpdateCustomerSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    phone_number: str
    genre: str
    user: UserSchema


class CustomerSchema(UpdateCustomerSchema):
    document_id: str


class ShowCustomerSchema(CustomerSchema):
    id: int
    role: str

    class Config:
        orm_mode = True
