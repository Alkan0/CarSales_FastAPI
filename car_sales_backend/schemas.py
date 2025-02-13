from pydantic import BaseModel, EmailStr
from typing import Optional

# Σχήμα για δημιουργία αυτοκινήτου
class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    price: int

# Σχήμα για επιστροφή αυτοκινήτου
class CarOut(BaseModel):
    id: int
    make: str
    model: str
    year: int
    price: int
    owner_id: int

    # Σχήμα για δημιουργία χρήστη
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_seller: bool = False

# Σχήμα για επιστροφή χρήστη (χωρίς password)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_seller: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class Config:
    from_attributes = True  # Χρήση ORM mode
