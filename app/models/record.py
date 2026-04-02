
from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class Record(BaseModel):
    id: int
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str
    date: date
    notes: str = ""
