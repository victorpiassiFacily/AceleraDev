from pydantic import BaseModel


class AdminSchema(BaseModel):
    display_name: str
    email: str
    password: str


class ShowAdminSchema(AdminSchema):
    id: int
    role: str

    class Config:
        orm_mode = True
