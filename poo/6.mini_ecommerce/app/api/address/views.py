from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Address
from app.repositories.address_repository import AddressRepository
from .schemas import AddressSchema, ShowAddressSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(address: AddressSchema, repository: AddressRepository = Depends()):
    repository.create(Address(**address.dict()))


@router.get('/', response_model=List[ShowAddressSchema])
def index(repository: AddressRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, address: AddressSchema, repository: AddressRepository = Depends()):
    repository.update(id, address.dict())


@router.get('/{id}')
def show(id: int, repository: AddressRepository = Depends()):
    return repository.get_by_id(id)


@router.delete('/{id}')
def delete(id: int, repository: AddressRepository = Depends()):
    repository.delete(id)
