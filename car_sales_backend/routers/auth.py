from fastapi import APIRouter, Depends, HTTPException
from car_sales_backend import models, schemas, database, auth
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
def login(user_data: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if not user or user.hashed_password != user_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
