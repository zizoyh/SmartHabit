# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

settings = get_settings()


# create SQLAlchemy engine which is our connection to the database in postgresql
engine = create_engine(settings.database_url)

# create a session factory which each instance will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for our models to inherit from
Base = declarative_base()

if __name__ == "__main__":
    # Quick test to confirm we can connect
    with engine.connect() as conn:
        print("Database connection OK:", conn)
