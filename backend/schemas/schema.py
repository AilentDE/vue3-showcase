from pydantic import BaseModel, UUID4
from typing import List

class CoachBase(BaseModel):
    firstName: str
    lastName: str
    areas: List[str]
    description: str
    hourlyRate: int

class RequestBase(BaseModel):
    coachId: UUID4
    userEmail: str
    message: str

class AuthBase(BaseModel):
    email: str
    password: str