from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import PaymentMethod
from .base_repository import BaseRepository


class PaymentMethodRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, PaymentMethod)

    def get_enabled_by_id(self, id: int):
        self.session.query(self.model).filter_by(
            id=id,
            enabled=True
        ).first()
