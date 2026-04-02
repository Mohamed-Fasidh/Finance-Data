
from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    id: int
    name: str
    role: Literal["viewer", "analyst", "admin"]
    active: bool = True
