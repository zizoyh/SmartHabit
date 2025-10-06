#app/models/user.py
# this file contains the User model definition using SQLAlchemy. maps to user table in the DB

# we import necessary modules from sqlalchemy and the Base class from database.py
from sqlalchemy import Column, Integer, String
# this is the base cass from database.py that our models will inherit from. it is needed for SQLAlchemy ORM to work
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"  # this is the name of the table in the database

    # define columns in the users table
    id = Column(Integer, primary_key=True, index=True)  # primary key column
    email = Column(String, unique=True, index=True, nullable=False)  # email column
    hashed_password = Column(String, nullable=False)  # hashed password column
    full_name = Column(String, nullable=True)  # full name column

    # now each user can have multiple habits, we define a relationship to the Habit model
    # user owns multiple habits and nudges
    habits = relationship("Habit", back_populates="user")

