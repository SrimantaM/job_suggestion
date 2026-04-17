from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(data: LoginRequest):
    # Replace this with real authentication logic
    if data.username != "admin" or data.password != "secret":
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {
        "message": "Login successful",
        "user": {"username": data.username},
        "access_token": "fake-jwt-token",
        "token_type": "bearer",
    }