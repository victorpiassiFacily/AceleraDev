from fastapi import FastAPI
from app.api.router import router
from app.models.models import Base
from app.db.db import engine

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(router)
