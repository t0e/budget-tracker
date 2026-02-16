from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId


class ExpenseBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str
    description: Optional[str] = None
    date: datetime


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    title: Optional[str]
    amount: Optional[float]
    category: Optional[str]
    description: Optional[str]
    date: Optional[datetime]


class ExpenseInDB(ExpenseBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
