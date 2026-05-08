from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

# Create the FastAPI application instance.
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.on_event("startup")
def on_startup():
    # Create database tables at app startup.
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    # Welcome route for the base URL.
    return {"message": f"Welcome to the {settings.app_name}"}


@app.get("/health")
def health_check():
    # Simple route to confirm the API is running.
    return {"message": "Smoking Tracker API is up and running"}