#app/models/nudge.py
# this file contains the Nudge model definition using SQLAlchemy. maps to nudges table in the DB
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime   
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean


class Nudge(Base):
    __tablename__ = "nudges"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    message = Column(String, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    delivered = Column(Boolean, default=False)
    nudge_type = Column(String, nullable=False)  # e.g., "reminder", "motivation"

    user = relationship("User", back_populates="nudges")
    habit = relationship("Habit", back_populates="nudges")

    #Habit ↔ HabitLog
    #User ↔ Habit
    #User ↔ Nudge
    #Habit ↔ Nudge