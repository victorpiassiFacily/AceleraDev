from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import ProductDiscount
from .base_repository import BaseRepository


class ProductDiscountRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, ProductDiscount)

    def get_by_payment_method_id(self, id: int):
        self.session.query(self.model).filter_by(
            payment_method_id=id
        ).first()
