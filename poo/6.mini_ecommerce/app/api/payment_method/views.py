from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import PaymentMethod
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.services.auth_service import only_admin, get_user
from .schemas import PaymentMethodSchema, ShowPaymentMethodSchema

router = APIRouter(dependencies=[Depends(only_admin)])


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodSchema, repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))


@router.get('/', response_model=List[ShowPaymentMethodSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, payment_method: PaymentMethodSchema, repository: PaymentMethodRepository = Depends()):
    repository.update(id, payment_method.dict())


@router.get('/{id}')
def show(id: int, repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)
