#app/models/habits.py
# this file contains the Habit model definition using SQLAlchemy. maps to habits table in the DB
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    # foreign key to link habit to a user, foreighn keys are used to establish relationships between tables
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    frequency = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to the User model
    # habit is owned by a user and each habit belongs to one user
    # habit owns nudges and logs
    user = relationship("User", back_populates="habits")

    nudges = relationship("Nudge", back_populates="habit")
