from typing import List
from fastapi import APIRouter, status, Depends, HTTPException

from app.repositories.product_discount_repository import ProductDiscountRepository
from app.services.product_discount_service import ProductDiscountService
from app.models.models import ProductDiscount
from .schemas import ProductDiscountSchema, ShowProductDiscountSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    product_discount: ProductDiscountSchema,
    service: ProductDiscountService = Depends(),
    repository: ProductDiscountRepository = Depends()
):
    try:
        service.check_discount(product_discount)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

    repository.create(ProductDiscount(**product_discount.dict()))


@router.get('/', response_model=List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(
    id: int,
    product_discount: ProductDiscountSchema,
    service: ProductDiscountService = Depends(),
    repository: ProductDiscountRepository = Depends()
):
    try:
        service.check_discount(product_discount)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

    repository.update(id, product_discount.dict())


@router.get('/{id}')
def show(id: int, repository: ProductDiscountRepository = Depends()):
    return repository.get_by_id(id)
