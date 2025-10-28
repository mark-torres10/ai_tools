from __future__ import annotations
from typing import Optional
from fastapi import APIRouter, HTTPException, Query

from ..data import store
from ..schemas import FeedResponse, PostWithAuthor

router = APIRouter(prefix="/feed", tags=["feed"])


@router.get("", response_model=FeedResponse)
def get_feed(cursor: Optional[str] = Query(None), limit: int = Query(20, ge=1, le=50)) -> FeedResponse:
    posts, next_cursor = store.get_feed(cursor=cursor, limit=limit)
    items: list[PostWithAuthor] = []
    for p in posts:
        author = store.get_profile(p.author_id)
        if author is None:
            raise HTTPException(status_code=500, detail="Author not found")
        items.append(PostWithAuthor(**p.model_dump(), author=author))
    return FeedResponse(items=items, next_cursor=next_cursor)
