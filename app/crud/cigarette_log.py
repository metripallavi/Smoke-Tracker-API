from datetime import datetime, time, timedelta

from sqlalchemy.orm import Session

from app.models.cigarette_log import CigaretteLog
from app.schemas.cigarette_log import CigaretteLogCreate


def create_cigarette_log(db: Session, user_id: int, data: CigaretteLogCreate):
    log = CigaretteLog(user_id=user_id, smoked_at=data.smoked_at)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_cigarette_logs_by_user(db: Session, user_id: int):
    return (
        db.query(CigaretteLog)
        .filter(CigaretteLog.user_id == user_id)
        .order_by(CigaretteLog.smoked_at.desc())
        .all()
    )


def get_today_cigarette_logs_by_user(db: Session, user_id: int):
    today = datetime.now().date()
    start_of_day = datetime.combine(today, time.min)
    end_of_day = start_of_day + timedelta(days=1)

    return (
        db.query(CigaretteLog)
        .filter(CigaretteLog.user_id == user_id)
        .filter(CigaretteLog.smoked_at >= start_of_day)
        .filter(CigaretteLog.smoked_at < end_of_day)
        .order_by(CigaretteLog.smoked_at.desc())
        .all()
    )


def get_cigarette_log_by_id(db: Session, log_id: int):
    return db.query(CigaretteLog).filter(CigaretteLog.id == log_id).first()

from sqlalchemy import func

def get_cigarette_log_summary_by_user(db: Session, user_id: int):
    total_logs = db.query(CigaretteLog).filter(CigaretteLog.user_id == user_id).count()

    today = datetime.now().date()
    start_of_day = datetime.combine(today, time.min)
    end_of_day = start_of_day + timedelta(days=1)

    today_logs = (
        db.query(CigaretteLog)
        .filter(CigaretteLog.user_id == user_id)
        .filter(CigaretteLog.smoked_at >= start_of_day)
        .filter(CigaretteLog.smoked_at < end_of_day)
        .count()
    )

    return {"total_logs": total_logs, "today_logs": today_logs}

def delete_cigarette_log(db: Session, log_id: int):
    log = get_cigarette_log_by_id(db, log_id)
    if not log:
        return None
    db.delete(log)
    db.commit()
    return log