import os
from fastapi import FastAPI
from car_sales_backend.routers import users, cars, auth
from car_sales_backend.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Test για το .env
print("✅ DATABASE_URL:", os.getenv("DATABASE_URL"))
print("✅ SECRET_KEY:", os.getenv("SECRET_KEY"))

# Προσθήκη των routers
app.include_router(users.router)
app.include_router(cars.router)
app.include_router(auth.router)
