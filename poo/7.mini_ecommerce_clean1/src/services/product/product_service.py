from src.domain.product.model import Product
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_product(description, price, technical_details, image, visible, category_id, supplier_id, uow: SqlAlchemyUnitOfWork):
    with uow:
        category = category_id
        supplier = supplier_id

        uow.product_repository.add(
            Product(
                description=description, price=price, technical_details=technical_details,
                image=image, visible=visible, category=category, supplier=supplier
            )
        )
        uow.commit()
