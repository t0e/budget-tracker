from pydantic import BaseModel

class TransactionCreate(BaseModel):
    description: str
    amount: float
    qty: int
    total_amount: float
    category_id: str
    date: str | None = None
    qty: int

class TransactionOut(BaseModel):
    id: str
    description: str
    amount: float
    qty: int
    total_amount: float
    date: str | None = None
    created_at: str
    updated_at: str
    category: dict | None = None