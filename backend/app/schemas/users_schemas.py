from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserPublicResponse(BaseModel):
    id: int
    email: EmailStr
    balance: float
    is_bankrupt: bool
    registered_at: datetime

    class Config:
        from_attributes = True