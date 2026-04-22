import asyncio
from datetime import datetime, UTC
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "budget_tracker"

categories = [
    { "name": "Eat Out", "icon": "🍽️", "color": "#FF6B6B", "type": "expense" },
    { "name": "Family", "icon": "👨‍👩‍👧", "color": "#6BCB77", "type": "expense" },
    { "name": "Utility", "icon": "💡", "color": "#4D96FF", "type": "expense" },
    { "name": "Subscription", "icon": "📺", "color": "#9D4EDD", "type": "expense" },
    { "name": "Cafe", "icon": "☕", "color": "#C77DFF", "type": "expense" },
    { "name": "Grocery", "icon": "🛒", "color": "#00C897", "type": "expense" },
    { "name": "Gasoline", "icon": "⛽", "color": "#FF922B", "type": "expense" },
    { "name": "Entertainment", "icon": "🎮", "color": "#F72585", "type": "expense" },
    { "name": "Personal", "icon": "🧴", "color": "#4895EF", "type": "expense" },
    { "name": "Rent", "icon": "🏠", "color": "#3A0CA3", "type": "expense" },
    { "name": "Health", "icon": "💊", "color": "#E63946", "type": "expense" },
    { "name": "Lend", "icon": "🤝", "color": "#2A9D8F", "type": "expense" }
]


async def seed():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    collection = db["categories"]

    # Optional: clear existing data
    await collection.delete_many({})

    # Add timestamps
    for c in categories:
        c["created_at"] = str(datetime.now(UTC))

    result = await collection.insert_many(categories)

    print(f"✅ Inserted {len(result.inserted_ids)} categories")

    client.close()


if __name__ == "__main__":
    asyncio.run(seed())