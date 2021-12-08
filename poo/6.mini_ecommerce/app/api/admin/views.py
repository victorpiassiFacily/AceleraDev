from typing import List
from fastapi import APIRouter, status, Depends

from app.models.models import User
from app.repositories.user_repository import UserRepository
from app.services.auth_service import only_admin, get_user
from .schemas import AdminSchema, ShowAdminSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(admin: AdminSchema, repository: UserRepository = Depends()):

    admin_dict = admin.dict()
    admin_dict["role"] = "admin"

    repository.create(User(**admin_dict))


@router.get('/', response_model=List[ShowAdminSchema])
def index(repository: UserRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, admin: AdminSchema, repository: UserRepository = Depends()):
    repository.update(id, admin.dict())


@router.get('/{id}')
def show(id: int, repository: UserRepository = Depends()):
    return repository.get_by_id(id)


@router.delete('/{id}')
def delete(id: int, repository: UserRepository = Depends()):
    repository.delete(id)
