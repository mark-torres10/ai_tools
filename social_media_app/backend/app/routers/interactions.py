from __future__ import annotations
from fastapi import APIRouter, HTTPException

from ..data import store
from ..schemas import LikeRequest, CommentRequest, ShareRequest, InteractionResponse

router = APIRouter(prefix="/posts", tags=["interactions"])


@router.post("/{post_id}/like", response_model=InteractionResponse)
def like_post(post_id: str, body: LikeRequest) -> InteractionResponse:
    if post_id not in store.posts:
        raise HTTPException(status_code=404, detail="Post not found")
    liked = store.toggle_like(post_id, body.user_id)
    post = store.posts[post_id]
    return InteractionResponse(post=post, liked_by_user=liked)


@router.post("/{post_id}/comment", response_model=InteractionResponse)
def comment_post(post_id: str, body: CommentRequest) -> InteractionResponse:
    if post_id not in store.posts:
        raise HTTPException(status_code=404, detail="Post not found")
    comment = store.add_comment(post_id, body.user_id, body.text)
    if comment is None:
        raise HTTPException(status_code=400, detail="Cannot add comment")
    post = store.posts[post_id]
    return InteractionResponse(post=post, new_comment=comment)


@router.post("/{post_id}/share", response_model=InteractionResponse)
def share_post(post_id: str, body: ShareRequest) -> InteractionResponse:
    if post_id not in store.posts:
        raise HTTPException(status_code=404, detail="Post not found")
    ok = store.add_share(post_id, body.user_id)
    if not ok:
        raise HTTPException(status_code=400, detail="Cannot share")
    post = store.posts[post_id]
    return InteractionResponse(post=post)
