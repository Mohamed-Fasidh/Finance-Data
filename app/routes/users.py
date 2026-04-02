from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.db_models import UserDB
from app.core.database import SessionLocal
from app.core.deps import get_current_user, check_role
from app.core.security import hash_password

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  CREATE USER (Admin only)
@router.post("/")
def create_user(
    name: str,
    email: str,
    password: str,
    role: str,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin"])

    new_user = UserDB(
        name=name,
        email=email,
        password=hash_password(password),
        role=role,
        active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


#  GET USERS (All roles)
@router.get("/")
def get_users(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin", "analyst", "viewer"])

    return db.query(UserDB).all()


#  UPDATE USER (Admin only)
@router.put("/{user_id}")
def update_user(
    user_id: int,
    name: str,
    role: str,
    active: bool,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin"])

    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = name
    db_user.role = role
    db_user.active = active

    db.commit()
    db.refresh(db_user)
    return db_user