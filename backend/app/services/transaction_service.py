from app.db.database import database
from app.models.transaction_model import transaction_model


async def create_transaction(data: dict):
    transaction = transaction_model(data)
    result = await database.transactions.insert_one(transaction)
    return {
        "id": str(result.inserted_id),
        **data
    }


async def get_transactions():
    pipeline = get_pipeline()
    cursor = database.transactions.aggregate(pipeline)
    results = []

    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        
        if "category_id" in doc:
            doc["category_id"] = str(doc["category_id"])

        if doc.get("category"):
            doc["category"]["id"] = str(doc["category"]["_id"])
            del doc["category"]["_id"]
        results.append(doc)

    return results

def get_pipeline() -> list:
    return [
        {
            "$lookup": {
                "from": "categories",
                "localField": "category_id",
                "foreignField": "_id",
                "as": "category"
            }
        },
        {
            "$unwind": {
                "path": "$category",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$sort": {"date": -1}
        }
    ]