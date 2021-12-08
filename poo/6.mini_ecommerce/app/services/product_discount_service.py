from fastapi import Depends
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.api.product_discount.schemas import ProductDiscountSchema


class ProductDiscountService:
    def __init__(
        self,
        payment_method_repository: PaymentMethodRepository = Depends(),
        product_discount_repository: ProductDiscountRepository = Depends()
    ):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def check_discount(self, product_discount: ProductDiscountSchema):

        used_method = self.product_discount_repository.get_by_payment_method_id(
            product_discount.payment_method_id
        )

        enabled = self.payment_method_repository.get_enabled_by_id(
            product_discount.payment_method_id
        )

        if used_method:
            raise Exception(
                "Ja existe um desconto para essa forma de pagamento"
            )
        if not enabled:
            raise Exception("Método de pagamento inativo!")
