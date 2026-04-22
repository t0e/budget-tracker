# 💰 Budgetly — Personal Budget Tracker

Budgetly is a modern personal finance tracking application that helps users manage expenses, track income, and stay within budget through a clean and intuitive interface.

---

## 🚀 Features

- 📊 Track income and expenses in real-time
- 🗂 Categorize transactions (food, rent, transport, etc.)
- 💡 Set monthly budgets and monitor spending
- 📈 Visualize financial data with charts and summaries
- 🔍 Filter and search transactions easily
- 📱 Responsive design for desktop and mobile

---

## 🧠 Tech Stack

**Frontend**

- React + TypeScript
- Redux Toolkit / Zustand (state management)
- React Router
- Tailwind CSS

**Backend**

- Python + FastAPI
- MongoDB

---

## 📂 Project Structure

```
budget-tracker/
├── backend/          # FastAPI backend
│   ├── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── main.py
│   └── Dockerfile
│
├── frontend/         # React frontend
│   ├── src/
│   ├── public/
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🐳 Running with Docker

### 1. Clone the repository

```bash id="s8b8tv"
git clone https://github.com/t0e/budget-tracker.git
cd budget-tracker
```

### 2. Run the app

```bash id="p81by3"
docker-compose up --build
```

---

## 🌐 Access the application

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs (Swagger): http://localhost:8000/docs

---

## 📸 Screenshots (optional)

_Add screenshots of your dashboard, charts, and transaction pages here._

---

## 📌 Author

**Thet Maung Maugn Toe**

- GitHub: https://github.com/t0e
