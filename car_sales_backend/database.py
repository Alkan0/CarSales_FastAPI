from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Σύνδεση με PostgreSQL από το Docker Compose
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/carsales")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
