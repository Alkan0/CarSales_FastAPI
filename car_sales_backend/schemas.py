from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_seller: bool


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_seller: bool

    class Config:
        orm_mode = True


class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price: int


class CarOut(CarCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
