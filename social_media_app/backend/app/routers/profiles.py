from __future__ import annotations
from fastapi import APIRouter, HTTPException

from ..data import store
from ..schemas import ProfileResponse

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/{profile_id}", response_model=ProfileResponse)
def get_profile(profile_id: str) -> ProfileResponse:
    profile = store.get_profile(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    posts = store.get_posts_by_author(profile_id)
    return ProfileResponse(profile=profile, posts=posts)
