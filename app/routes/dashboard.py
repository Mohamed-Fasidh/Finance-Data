from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from collections import defaultdict

from app.models.db_models import RecordDB
from app.core.database import SessionLocal
from app.core.deps import get_current_user, check_role

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  SUMMARY
@router.get("/summary")
def summary(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin", "analyst", "viewer"])

    records = db.query(RecordDB).all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    category_totals = defaultdict(float)
    for r in records:
        category_totals[r.category] += r.amount

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense,
        "category_breakdown": dict(category_totals),
        "total_records": len(records)
    }


#  RECENT ACTIVITY
@router.get("/recent")
def recent_activity(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin", "analyst", "viewer"])

    records = db.query(RecordDB).order_by(RecordDB.date.desc()).limit(5).all()
    return records


#  MONTHLY TRENDS
@router.get("/monthly-trends")
def monthly_trends(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    check_role(user, ["admin", "analyst", "viewer"])

    records = db.query(RecordDB).all()

    trends = defaultdict(float)

    for r in records:
        month = r.date.strftime("%Y-%m")

        if r.type == "income":
            trends[month] += r.amount
        else:
            trends[month] -= r.amount

    return dict(trends)