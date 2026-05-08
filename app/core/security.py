from passlib.context import CryptContext

# Password hashing configuration.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    # Hash a plain password before saving it.
    return pwd_context.hash(password)