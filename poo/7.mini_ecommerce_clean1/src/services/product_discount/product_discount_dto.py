from dataclasses import dataclass


@dataclass
class ProductDiscountDTO:
    mode: str
    value: float
    payment_method_id: int
    product_id: int
