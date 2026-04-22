import asyncio
import os
import random
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "budget_tracker"

# realistic notes
NOTES = {
    "Eat Out": ["Lunch", "Dinner with friends", "Street food"],
    "Cafe": ["Coffee", "Latte", "Work at cafe"],
    "Grocery": ["Supermarket", "Weekly groceries"],
    "Gasoline": ["Fuel refill"],
    "Entertainment": ["Movie", "Games"],
    "Utility": ["Electric bill", "Water bill"],
    "Subscription": ["Netflix", "Spotify"],
    "Personal": ["Clothes", "Haircut"],
    "Health": ["Medicine", "Doctor visit"],
    "Rent": ["Monthly rent"],
    "Family": ["Send money home"],
    "Lend": ["Lent to friend"]
}


def random_date():
    now = datetime.utcnow()
    return now - timedelta(days=random.randint(0, 30))


def random_amount(category):
    ranges = {
        "Eat Out": (50000, 200000),
        "Cafe": (30000, 100000),
        "Grocery": (100000, 500000),
        "Gasoline": (50000, 150000),
        "Entertainment": (100000, 400000),
        "Utility": (200000, 800000),
        "Subscription": (50000, 200000),
        "Personal": (100000, 500000),
        "Health": (100000, 600000),
        "Rent": (2000000, 5000000),
        "Family": (500000, 2000000),
        "Lend": (100000, 1000000)
    }
    low, high = ranges.get(category, (50000, 200000))
    return random.randint(low, high)


async def seed():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]

    transactions_col = db["transactions"]
    categories_col = db["categories"]

    categories = await categories_col.find().to_list(length=100)

    if not categories:
        print("❌ No categories found. Seed categories first.")
        return

    transactions = []

    for _ in range(50):  # generate 50 transactions
        category = random.choice(categories)

        name = category["name"]

        qty = random.choices(
            population=[1, 2, 3],
            weights=[0.8, 0.15, 0.05],  # 80% chance = 1
            k=1
        )[0]

        amount = random_amount(name)

        transaction = {
            "amount": amount,
            "qty": qty,
            "total_amount": qty * amount,
            "type": "expense",
            "category_id": str(category["_id"]),
            "category_id": ObjectId(category["_id"]),
            "note": random.choice(NOTES.get(name, ["Expense"])),
            "date": random_date(),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }

        transactions.append(transaction)

    await transactions_col.insert_many(transactions)

    print(f"✅ Inserted {len(transactions)} transactions")

    client.close()


if __name__ == "__main__":
    asyncio.run(seed())