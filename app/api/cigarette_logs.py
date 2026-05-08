from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.cigarette_log import CigaretteLogCreate, CigaretteLogResponse, CigaretteLogSummaryResponse
from app.crud.cigarette_log import get_cigarette_log_summary_by_user

from app.db.deps import get_db, get_current_user
from app.crud.cigarette_log import (
    create_cigarette_log,
    get_cigarette_logs_by_user,
    delete_cigarette_log,
    get_cigarette_log_by_id,
    get_today_cigarette_logs_by_user,
)
from app.models.user import User
from app.schemas.cigarette_log import CigaretteLogCreate, CigaretteLogResponse

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.post("/", response_model=CigaretteLogResponse, status_code=status.HTTP_201_CREATED)
def add_log(
    data: CigaretteLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_cigarette_log(db, current_user.id, data)


@router.get("/", response_model=list[CigaretteLogResponse])
def list_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_cigarette_logs_by_user(db, current_user.id)


@router.get("/today", response_model=list[CigaretteLogResponse])
def list_today_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_today_cigarette_logs_by_user(db, current_user.id)


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_log(
    log_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    log = get_cigarette_log_by_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    if log.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to delete this log")
    delete_cigarette_log(db, log_id)
    return None

@router.get("/summary", response_model=CigaretteLogSummaryResponse)
def log_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_cigarette_log_summary_by_user(db, current_user.id)