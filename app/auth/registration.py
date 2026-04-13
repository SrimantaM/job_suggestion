from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pydantic.networks import EmailStr

router = APIRouter(prefix="/auth", tags=["auth"])

class RegistrationRequest(BaseModel):
    username: str
    email: EmailStr
    password: str




@router.post("/register")
async def register(data: RegistrationRequest):
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Username and password are required")

    # TODO: add real persistence + password hashing
    return {
        "message": "Registration successful",
        "user": {
            "username": data.username,
            "email": data.email,
        },
    }
