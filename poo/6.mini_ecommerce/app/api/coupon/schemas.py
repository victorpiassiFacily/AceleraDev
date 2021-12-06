from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class CouponEnum(str, Enum):
    value = "value"
    percentage = "percentage"


class UpdateCouponSchema(BaseModel):
    limit: int
    expire_at: datetime


class CouponSchema(UpdateCouponSchema):
    code: str
    type: CouponEnum
    value: float


class ShowCouponSchema(CouponSchema):
    id: int

    class Config:
        orm_mode = True
