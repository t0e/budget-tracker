from fastapi import APIRouter
from app.schemas.transaction_schema import TransactionCreate
from app.services.transaction_service import (
    create_transaction,
    get_transactions
)

router = APIRouter()

@router.post("/")
async def create(data: TransactionCreate):
    return await create_transaction(data.model_dump())

@router.get("/")
async def list_transactions():
    return await get_transactions()
