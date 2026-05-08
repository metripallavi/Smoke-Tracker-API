from collections.abc import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    # Provide a database session to each request.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()