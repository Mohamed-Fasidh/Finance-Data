from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.models.db_models import RecordDB, UserDB
from app.core.database import SessionLocal
from app.core.deps import get_current_user, check_role
from app.schemas.record import RecordCreate
from app.core.response import success_response
from app.services.record_service import create_record_service

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  CREATE RECORD (Admin only)
@router.post("/")
def create_record(
    data: RecordCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin"])

    #  get current DB user
    db_user = db.query(UserDB).filter(UserDB.email == user["sub"]).first()

    record = create_record_service(db, data, db_user.id)

    return success_response(record, "Record created")


#  GET RECORDS (All roles + filtering + pagination)
@router.get("/")
def get_records(
    type: Optional[str] = None,
    category: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin", "analyst", "viewer"])

    db_user = db.query(UserDB).filter(UserDB.email == user["sub"]).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Role-based access
    if user["role"] == "admin":
        query = db.query(RecordDB)
    elif user["role"] in ["analyst", "viewer"]:
        query = db.query(RecordDB)

    if type:
        query = query.filter(RecordDB.type == type)

    if category:
        query = query.filter(RecordDB.category == category)

    offset = (page - 1) * limit
    records = query.offset(offset).limit(limit).all()

    return success_response(records)


#  UPDATE RECORD (Admin only)
@router.put("/{record_id}")
def update_record(
    record_id: int,
    data: RecordCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin"])

    db_user = db.query(UserDB).filter(UserDB.email == user["sub"]).first()

    record = db.query(RecordDB).filter(
        RecordDB.id == record_id,
        RecordDB.user_id == db_user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    record.amount = data.amount
    record.type = data.type
    record.category = data.category
    record.date = data.date
    record.notes = data.notes

    db.commit()
    db.refresh(record)

    return success_response(record, "Record updated")


#  DELETE RECORD (Admin only)
@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin"])

    db_user = db.query(UserDB).filter(UserDB.email == user["sub"]).first()

    record = db.query(RecordDB).filter(
        RecordDB.id == record_id,
        RecordDB.user_id == db_user.id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return success_response(None, "Record deleted")