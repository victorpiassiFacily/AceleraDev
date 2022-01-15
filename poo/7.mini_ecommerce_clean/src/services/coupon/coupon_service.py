from src.domain.coupon.model import Coupon
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_coupon(code, expire_at, limit, type, value, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.coupon_repository.add(
            Coupon(
                code=code, expire_at=expire_at,
                limit=limit, type=type, value=value
            )
        )
        uow.commit()
