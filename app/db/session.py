from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create the SQLAlchemy engine from the database URL.
engine = create_engine(settings.database_url)

# Create a session factory for database operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)