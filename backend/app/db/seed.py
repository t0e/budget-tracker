import asyncio
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "budget_tracker"

sample_data = [
    {
        "date": datetime(2025, 2, 1),
        "description": "Lunch at restaurant",
        "category": "Food",
        "qty": 1,
        "total_amount": 12.5,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    },
    {
        "date": datetime(2025, 2, 2),
        "description": "Bus ticket",
        "category": "Transport",
        "qty": 2,
        "total_amount": 5.0,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    },
    {
        "date": datetime(2025, 2, 3),
        "description": "Groceries",
        "category": "Food",
        "qty": 12,
        "total_amount": 84.2,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }
]

async def seed():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DATABASE_NAME]
    await db.expenses.insert_many(sample_data)
    print("Sample expenses inserted!")

asyncio.run(seed())
