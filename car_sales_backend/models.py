from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from car_sales_backend.database import Base

# Μοντέλο Χρήστη
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_seller = Column(Boolean, default=False)

    cars = relationship("Car", back_populates="owner")

# Μοντέλο Αυτοκινήτου
class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)   # Μάρκα (π.χ. Toyota)
    model = Column(String, index=True)  # Μοντέλο (π.χ. Corolla)
    year = Column(Integer)              # Έτος κατασκευής
    price = Column(Integer)             # Τιμή πώλησης

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="cars")
