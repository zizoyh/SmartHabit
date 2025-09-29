# SmartHabit
SmartHabit API is a FastAPI-based backend that helps users create, track, and analyze daily habits. It offers JWT-secured REST endpoints for habit management, streak tracking, and weekly insights, plus Celery/Redis-powered predictive analytics and personalized nudges. Deployed on AWS with Docker and CI/CD for scalability.

ChatGPT Generated Outline:
Here’s a **clean, scalable project structure and roadmap** for your **SmartHabit API**.
This design is production-ready, easy to test, and follows modern FastAPI practices.

---

## 🗂 Folder / File Structure

```
smarthabit-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   ├── config.py               # Settings (DB URL, JWT secret, etc.)
│   │
│   ├── api/                    # Route definitions
│   │   ├── __init__.py
│   │   ├── users.py            # /users endpoints
│   │   ├── habits.py           # /habits endpoints
│   │   ├── insights.py         # /insights and /nudges endpoints
│   │
│   ├── core/                   # Core utilities
│   │   ├── __init__.py
│   │   ├── security.py         # JWT helpers (token creation, password hashing)
│   │   ├── celery_app.py       # Celery/Redis configuration
│   │   ├── scheduler.py        # Background tasks & reminders
│   │
│   ├── models/                 # Database ORM models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── habit.py
│   │   ├── habit_log.py
│   │   ├── nudge.py
│   │
│   ├── schemas/                # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── habit_schema.py
│   │   ├── nudge_schema.py
│   │
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── habit_service.py
│   │   ├── nudge_service.py
│   │   ├── insight_service.py
│   │
│   └── database.py             # SQLAlchemy session + base metadata
│
├── tests/                      # Unit & integration tests
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_habits.py
│   ├── test_nudges.py
│
├── alembic/                    # Migrations (if using Alembic)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt            # Python dependencies
├── .env                        # Secrets & environment variables (gitignored)
├── .gitignore
└── README.md
```

---

## 🏗️ General Project Outline / Build Roadmap

### 1️⃣ Initialization

* Create a new GitHub repo (`smarthabit-api`)
* Set up virtual environment and install dependencies:

  ```bash
  fastapi uvicorn sqlalchemy psycopg2-binary pydantic[dotenv] python-jose passlib[bcrypt] celery redis alembic pytest
  ```
* Create `.env` with database URL, JWT secret, etc.

---

### 2️⃣ Core Setup

* **main.py**: initialize FastAPI, include routers, handle CORS
* **config.py**: load environment variables (database URL, Redis URL)
* **database.py**: configure SQLAlchemy engine and session

---

### 3️⃣ User Management

* `models/user.py` & `schemas/user_schema.py`
* `api/users.py` routes:

  * `POST /users/register`
  * `POST /users/login`
* `core/security.py`: password hashing (Passlib), JWT token generation

---

### 4️⃣ Habit CRUD & Logs

* `models/habit.py`, `models/habit_log.py`
* `schemas/habit_schema.py`
* `api/habits.py` endpoints:

  * `POST /habits` (create habit)
  * `GET /habits` (list habits)
  * `POST /habits/{id}/checkin` (daily check-in)
* `services/habit_service.py` to calculate streaks

---

### 5️⃣ Insights & Nudges

* `models/nudge.py`, `schemas/nudge_schema.py`
* `api/insights.py` endpoints:

  * `GET /insights/weekly` (analytics)
  * `GET /nudges` (predictive suggestions)
* `services/nudge_service.py`: compute skip probability (simple ML/statistics)

---

### 6️⃣ Background Tasks

* `core/celery_app.py`: set up Celery with Redis broker
* `core/scheduler.py`: periodic jobs

  * e.g., daily streak recalculation, sending nudges

---

### 7️⃣ Testing & CI/CD

* Unit tests in `tests/` using pytest
* Integration tests with a test database
* GitHub Actions workflow to run tests on each push

---

### 8️⃣ Deployment

* Dockerfile & docker-compose.yml (FastAPI + PostgreSQL + Redis)
* Deploy to **AWS (EC2/RDS/Elastic Beanstalk)** or **Render/Heroku**
* Configure automatic migrations (Alembic)

---

## 🚀 Optional Enhancements

* Add a lightweight **React/Next.js** dashboard for habit visualization
* Integrate **Google Calendar** reminders (`api/integrations.py`)
* Add badges/gamification tables for long streaks

---

Would you like me to draft the **requirements.txt** with exact package versions and a starter `main.py` so you can spin up the API immediately?
