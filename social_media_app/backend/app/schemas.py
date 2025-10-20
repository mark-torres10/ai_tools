from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field


class Profile(BaseModel):
    id: str
    handle: str
    display_name: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class Comment(BaseModel):
    id: str
    post_id: str
    user_id: str
    text: str
    created_at: str


class Post(BaseModel):
    id: str
    author_id: str
    text: str
    created_at: str
    like_count: int = 0
    comment_count: int = 0
    share_count: int = 0


class PostWithAuthor(Post):
    author: Profile


class FeedResponse(BaseModel):
    items: List[PostWithAuthor]
    next_cursor: Optional[str] = None


class ProfileResponse(BaseModel):
    profile: Profile
    posts: List[Post]


class LikeRequest(BaseModel):
    user_id: str = Field(..., description="ID of the user performing the like action")


class CommentRequest(BaseModel):
    user_id: str
    text: str


class ShareRequest(BaseModel):
    user_id: str


class InteractionResponse(BaseModel):
    post: Post
    liked_by_user: Optional[bool] = None
    new_comment: Optional[Comment] = None
