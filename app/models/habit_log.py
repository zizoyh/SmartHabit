#app/models/habit_log.py
# this file contains the HabitLog model definition using SQLAlchemy. maps to habit_logs table in the DB
# this file is used to log when a habit is completed
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    completed_at = Column(DateTime, default=datetime.utcnow)

    #each habit_log belongs to one habit
    habit = relationship("Habit", back_populates="logs")
