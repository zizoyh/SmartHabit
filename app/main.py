# import fastapi
from fastapi import FastAPI
from app.config import get_settings

#create fastapi instance
app = FastAPI(
    title="SmartHabit API",
    description="API for SmartHabit application",
    version="0.1.0"
)

# temporary root endpoint we need to test server
# after we run "uvicorn main:app --reload" we'll see this message
@app.get("/")
def read_root():
    settings = get_settings()
    return {"message": "Welcome to SmartHabit API!"
            , "environment": settings.environment,
            "database_url": settings.database_url}