from typing import Dict, List
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


class UserLoginInfo(BaseModel):
    user_id: int
    username: str
    last_login: str


class JobStatItem(BaseModel):
    job_title: str
    applied: int
    shortlisted: int
    rejected: int
    interviews: int


class ResumeSuggestion(BaseModel):
    field: str
    suggestion: str


class DashboardResponse(BaseModel):
    logged_in_users: List[UserLoginInfo]
    job_stats: Dict[str, Dict[str, int]]
    resume_edit_suggestions: List[ResumeSuggestion]


@router.get("/", response_model=DashboardResponse)
async def get_dashboard():
    # Replace these with actual DB/service calls
    logged_in_users = [
        {"user_id": 1, "username": "alice", "last_login": "2026-04-13T09:21:00Z"},
        {"user_id": 2, "username": "bob", "last_login": "2026-04-13T09:45:00Z"},
    ]

    job_stats = {
        "alice": {"applied": 5, "shortlisted": 2, "rejected": 1, "interviews": 1},
        "bob": {"applied": 3, "shortlisted": 1, "rejected": 0, "interviews": 1},
    }

    resume_edit_suggestions = [
        {"field": "Summary", "suggestion": "Make your summary more specific to the target role."},
        {"field": "Skills", "suggestion": "Add technology keywords from the job description."},
    ]

    return {
        "logged_in_users": logged_in_users,
        "job_stats": job_stats,
        "resume_edit_suggestions": resume_edit_suggestions,
    }