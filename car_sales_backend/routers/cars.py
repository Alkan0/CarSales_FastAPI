from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from car_sales_backend.database import SessionLocal
from car_sales_backend import models, schemas, auth  # ✅ Σωστό import

router = APIRouter(prefix="/cars", tags=["Cars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
