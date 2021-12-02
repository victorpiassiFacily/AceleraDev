from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import ProductDiscount, PaymentMethod
from .schemas import ProductDiscountSchema, ShowProductDiscountSchema
from sqlalchemy.orm import Session
from app.db.db import get_db

router = APIRouter()


def check_payment_method(db, product_discount: ProductDiscountSchema):

    used_method = db.query(ProductDiscount).filter_by(
        payment_method_id=product_discount.payment_method_id
    ).first()

    enabled = db.query(PaymentMethod).filter_by(
        id=product_discount.payment_method_id,
        enabled=True
    ).first()

    if used_method:
        return {"message": "Método de pagamento já utilizado para desconto!"}
    if not enabled:
        return {"message": "Método de pagamento inativo!"}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, db: Session = Depends(get_db)):

    error = check_payment_method(db, product_discount)
    if error:
        return error

    db.add(ProductDiscount(**product_discount.dict()))
    db.commit()


@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(db: Session = Depends(get_db)):

    return db.query(ProductDiscount).all()


@router.put('/{id}')
def update(id: int, product_discount: ProductDiscountSchema, db: Session = Depends(get_db)):

    error = check_payment_method(db, product_discount)
    if error:
        return error

    query = db.query(ProductDiscount).filter_by(id=id)
    query.update(product_discount.dict())
    db.commit()


@router.get('/{id}')
def show(id: int, db: Session = Depends(get_db)):
    return db.query(ProductDiscount).filter_by(id=id).first()

# @router.delete('/{id}'):
# def delete():
#     pass
