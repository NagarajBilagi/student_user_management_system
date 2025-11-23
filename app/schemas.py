from pydantic import BaseModel, ConfigDict
from typing import Optional

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    selected_interest: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class InterestSelectRequest(BaseModel):
    interest: str

class InterestResourceResponse(BaseModel):
    interest_tag: str
    workshops: Optional[str]
    training: Optional[str]
    event: Optional[str]
    model_config = ConfigDict(from_attributes=True)
