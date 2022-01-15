from src.domain.product.model import Product
from src.domain.product_discount.model import ProductDiscount
from src.services.product.product_dto import ProductDiscountDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_discount(mode: str, value: float, payment_method_id: int, product_id: int, uow: SqlAlchemyUnitOfWork):
    with uow:
        product = uow.product_repository.get(id=product_id)

        if not product:
            raise Exception('Product not found')

        payment_method = uow.payment_method_repository.get(
            id=payment_method_id)

        if not payment_method:
            raise Exception('Payment method not found')

        discount = ProductDiscount(
            mode=mode, value=value, payment_method=payment_method)
        product.add_discount(discount)

        uow.commit()
