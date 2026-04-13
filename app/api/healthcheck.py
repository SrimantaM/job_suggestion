from fastapi import APIRouter


router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])

@router.get("/")
async def health_check():
    return {"status": "ok", "message": "API is healthy and running!"}