from pydantic import BaseModel
from datetime import date

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str

class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    notes: str
    user_id: int

    class Config:
        from_attributes = True