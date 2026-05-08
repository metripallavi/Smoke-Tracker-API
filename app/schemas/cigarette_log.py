from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CigaretteLogCreate(BaseModel):
    smoked_at: datetime | None = None


class CigaretteLogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    smoked_at: datetime

class CigaretteLogSummaryResponse(BaseModel):
    total_logs: int
    today_logs: int