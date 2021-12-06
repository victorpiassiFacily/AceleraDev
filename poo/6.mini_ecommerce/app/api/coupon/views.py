from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Coupon
from app.repositories.coupon_repository import CouponRepository
from .schemas import CouponSchema, ShowCouponSchema, UpdateCouponSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupon: CouponSchema, repository: CouponRepository = Depends()):
    repository.create(Coupon(**coupon.dict()))


@router.get('/', response_model=List[ShowCouponSchema])
def index(repository: CouponRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, coupon: CouponSchema, repository: UpdateCouponSchema = Depends()):
    repository.update(id, coupon.dict())


@router.get('/{id}')
def show(id: int, repository: CouponRepository = Depends()):
    return repository.get_by_id(id)


@router.delete('/{id}')
def delete(id: int, repository: CouponRepository = Depends()):
    repository.delete(id)
