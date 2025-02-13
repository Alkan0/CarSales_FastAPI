from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from car_sales_backend.database import SessionLocal
from car_sales_backend import models, schemas
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["Users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password, is_seller=user.is_seller)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
