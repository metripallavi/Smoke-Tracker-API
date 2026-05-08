from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.cigarette_logs import router as logs_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine, get_db
from app.models.cigarette_log import CigaretteLog  # noqa: F401
from app.models.user import User  # noqa: F401
from app.schemas.user import UserResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
    description="A FastAPI backend for smoking tracking.\n\n---\n\n💙 **Quit smoking because your family loves you.** 🙂💖",
)


@app.get("/")
def read_root():
    return {"message": f"Welcome to the {settings.app_name}"}


@app.get("/health")
def health_check():
    return {"message": "Smoking Tracker API is up and running"}


@app.get("/users", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()


app.include_router(users_router)
app.include_router(auth_router)
app.include_router(logs_router)