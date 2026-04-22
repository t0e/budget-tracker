from datetime import datetime
from bson import ObjectId

def transaction_model(transaction: dict) -> dict:
        return {
            "amount": transaction['amount'],
            "total_amount": transaction['total_amount'],
            "type": transaction['type'],
            "category_id": ObjectId(transaction["category_id"]),
            "qty": transaction.get("qty", 1),
            "note": transaction['note'],
            "date": transaction['date'],
            "created_at": transaction['created_at'],
            "updated_at": transaction['updated_at']
        }
