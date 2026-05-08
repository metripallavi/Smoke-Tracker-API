from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str):
    # Find a user by email.
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    # Find a user by username.
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate) -> User:
    # Create a new user with a hashed password.
    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password,
        is_active=True,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user