# app/database.py
# this file sets up the database connection using SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import get_settings

settings = get_settings()

# Create SQLAlchemy engine (connects to PostgreSQL)
engine = create_engine(settings.database_url)

# Session factory — each instance is an independent DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that ORM models inherit from
Base = declarative_base()

# Quick test if file is run directly
if __name__ == "__main__":
    with engine.connect() as conn:
        print("Database connection OK:", conn)
