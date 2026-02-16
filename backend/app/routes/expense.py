from fastapi import APIRouter
from app.db.database import expense_collection
from app.models.expense_model import expense_helper

router = APIRouter()

@router.get("")
async def get_expenses():
    expenses = []
    cursor = expense_collection.find().sort("date", -1)
    async for document in cursor:
        expenses.append(expense_helper(document))
    return expenses
