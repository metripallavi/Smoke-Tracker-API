from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    # Base class for all SQLAlchemy ORM models.
    pass


# Import models here so SQLAlchemy is aware of them before table creation.
from app.models.cigarette_log import CigaretteLog  # noqa: F401,E402
from app.models.user import User  # noqa: F401,E402