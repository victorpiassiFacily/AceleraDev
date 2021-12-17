from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Customer, User
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService
from app.services.user_service import UserService
from .schemas import CustomerSchema, ShowCustomerSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    customer: CustomerSchema,
    repository: CustomerRepository = Depends(),
    service: CustomerService = Depends(),
    user_service: UserService = Depends(),
):
    user_id = user_service.create_customer_user(customer.user)
    customer_data = service.customer_configure(customer, user_id)
    return repository.create(Customer(**customer_data))


@router.get('/', response_model=List[ShowCustomerSchema])
def index(repository: CustomerRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(
    id: int, customer: CustomerSchema,
    repository: CustomerRepository = Depends(),
    user_service: UserService = Depends()
):
    user_service.update_user(customer.user)
    return repository.update(id, customer.dict())


@router.get('/{id}')
def show(id: int, repository: CustomerRepository = Depends()):
    return repository.get_by_id(id)
