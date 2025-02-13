from fastapi import FastAPI
from car_sales_backend.database import engine, Base
from car_sales_backend.routers import users, cars, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(cars.router)
app.include_router(auth.router)  # 🔹 Προσθέσαμε το Authentication Router

@app.get("/")
def home():
    return {"message": "Welcome to Car Sales API"}
