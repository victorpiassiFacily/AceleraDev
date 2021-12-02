from pydantic import BaseModel
from enum import Enum

from app.api.payment_method.schemas import ShowPaymentMethodSchema
from app.api.product.schemas import ShowProductSchema


class ModeEnum(str, Enum):
    value = "value"
    percentage = "percentage"


class ProductDiscountSchema(BaseModel):
    mode: ModeEnum
    value: float
    product_id: int
    payment_method_id: int


class ShowProductDiscountSchema(ProductDiscountSchema):
    id: int

    payment_method: ShowPaymentMethodSchema
    product: ShowProductSchema

    class Config:
        orm_mode = True
