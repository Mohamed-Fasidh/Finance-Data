from app.models.db_models import UserDB
from app.core.security import hash_password

def create_user_service(db, data):
    user = UserDB(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role,
        active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user