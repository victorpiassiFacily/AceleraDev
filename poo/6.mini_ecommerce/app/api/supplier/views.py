from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import Supplier
from app.repositories.supplier_repository import SupplierRepository
from app.services.auth_service import only_admin, get_user
from .schemas import SupplierSchema, ShowSupplierSchema

router = APIRouter(dependencies=[Depends(only_admin)])


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))


@router.get('/', response_model=List[ShowSupplierSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, supplier: SupplierSchema, repository: SupplierRepository = Depends()):
    repository.update(id, supplier.dict())


@router.get('/{id}')
def show(id: int, repository: SupplierRepository = Depends()):
    return repository.get_by_id(id)
