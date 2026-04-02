from sqlalchemy import Column, Integer, String, Boolean, Float, Date, ForeignKey
from app.core.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    active = Column(Boolean, default=True)


class RecordDB(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    date = Column(Date)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))