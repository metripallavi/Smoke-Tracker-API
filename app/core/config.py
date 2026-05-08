from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Basic app settings.
    app_name: str = "Smoking Tracker API"
    app_version: str = "0.1.0"
    debug: bool = True

    # PostgreSQL connection string.
    database_url: str = "postgresql+psycopg2://postgres:admin@localhost:5432/smoke_tracker_db"

    # JWT settings.
    secret_key: str = "long-random-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()