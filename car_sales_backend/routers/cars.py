from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from car_sales_backend.database import SessionLocal
from car_sales_backend import models, schemas, auth, database

router = APIRouter(prefix="/cars", tags=["Cars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.CarOut])
def get_cars(db: Session = Depends(database.get_db)):
    cars = db.query(models.Car).all()
    return cars

@router.get("/{car_id}", response_model=schemas.CarOut)
def get_car(car_id: int, db: Session = Depends(database.get_db)):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/", response_model=schemas.CarOut)
def create_car(
    car: schemas.CarCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    new_car = models.Car(**car.dict(), owner_id=current_user.id)
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car
