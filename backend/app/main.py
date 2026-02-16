from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import expense

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])

@app.get("/")
async def root():
    return {"message": "FastAPI is running"}
