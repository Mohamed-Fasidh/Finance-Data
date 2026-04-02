from app.models.db_models import RecordDB

def create_record_service(db, record_data, user_id):
    record = RecordDB(
        amount=record_data.amount,
        type=record_data.type,
        category=record_data.category,
        date=record_data.date,
        notes=record_data.notes,
        user_id=user_id
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record