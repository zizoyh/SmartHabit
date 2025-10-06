# create_tables.py
from app.database import engine, Base
from app.models.user import User
from app.models.habits import Habit
from app.models.habit_log import HabitLog
from app.models.nudge import Nudge

print("Creating all database tables...")
Base.metadata.create_all(bind=engine)
print("Done ✅")
