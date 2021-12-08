from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Address
from .base_repository import BaseRepository


class AddressRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Address)

    def get_customer_primary_address(self, id):
        primary_address = self.session.query(
            self.model
        ).filter_by(customer_id=id).first()

        return primary_address
