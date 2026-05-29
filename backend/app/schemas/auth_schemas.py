#Defines data formats using Pydantic
#validate incoming data
#define request structure
#define response structure

from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    email: EmailStr
    username: str
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    balance: float
    is_bankrupt: bool

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer" # The type of the token. HTTP Authorization scheme. Typically "bearer" for JWT tokens.
    #Token type tells the backend how to interpret the token and how to use it for authentication.