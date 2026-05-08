from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CigaretteLogCreate(BaseModel):
    smoked_at: datetime | None = None


class CigaretteLogResponse(BaseModel):
    id: int
    user_id: int
    smoked_at: datetime

    model_config = ConfigDict(from_attributes=True)