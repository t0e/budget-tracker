from datetime import datetime
from bson import ObjectId

def expense_helper(expense) -> dict:
    return {
        "id": str(expense["_id"]),
        "date": expense["date"],
        "description": expense["description"],
        "category": expense["category"],
        "qty": expense["qty"],
        "total_amount": expense["total_amount"],
        "created_at": expense["created_at"],
        "updated_at": expense["updated_at"],
    }

# def create_expense_dict(data: dict) -> dict:
#     return {
#         "title": data["title"],
#         "amount": data["amount"],
#         "category": data["category"],
#         "description": data.get("description"),
#         "date": data["date"],
#         "created_at": datetime.utcnow(),
#         "updated_at": datetime.utcnow(),
#     }
