from __future__ import annotations
from typing import Dict, List, Optional, Tuple
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import string

from .schemas import Profile, Post, Comment


class InMemoryStore:
    def __init__(self) -> None:
        self.profiles: Dict[str, Profile] = {}
        self.posts: Dict[str, Post] = {}
        self.post_ids_ordered: List[str] = []
        self.comments: Dict[str, List[Comment]] = {}
        self.likes: Dict[str, set[str]] = {}
        self.shares: Dict[str, set[str]] = {}

    def seed(self, num_profiles: int = 12, num_posts: int = 100) -> None:
        random.seed(42)

        # Create profiles
        for i in range(num_profiles):
            profile_id = f"u{i+1:02d}"
            handle = f"user{i+1:02d}"
            display_name = f"User {i+1:02d}"
            bio = f"This is bio for {display_name}."
            avatar_url = f"https://api.dicebear.com/7.x/identicon/svg?seed={handle}"
            profile = Profile(
                id=profile_id,
                handle=handle,
                display_name=display_name,
                bio=bio,
                avatar_url=avatar_url,
            )
            self.profiles[profile_id] = profile

        # Create posts (reverse chronological)
        now = datetime.utcnow()
        for i in range(num_posts):
            author_id = random.choice(list(self.profiles.keys()))
            post_id = f"p{i+1:03d}"
            text = self._random_sentence(12 + (i % 12))
            created_at = (now - timedelta(minutes=i)).isoformat() + "Z"
            post = Post(
                id=post_id,
                author_id=author_id,
                text=text,
                created_at=created_at,
                like_count=0,
                comment_count=0,
                share_count=0,
            )
            self.posts[post_id] = post
            self.post_ids_ordered.append(post_id)
            self.comments[post_id] = []
            self.likes[post_id] = set()
            self.shares[post_id] = set()

        # Seed random interactions
        user_ids = list(self.profiles.keys())
        for post_id in self.post_ids_ordered:
            # Likes
            like_users = random.sample(user_ids, k=random.randint(0, min(8, len(user_ids))))
            for uid in like_users:
                self.likes[post_id].add(uid)
            self.posts[post_id].like_count = len(self.likes[post_id])

            # Comments
            for _ in range(random.randint(0, 3)):
                commenter = random.choice(user_ids)
                comment = Comment(
                    id=f"c{post_id}-{random.randint(1,10_000)}",
                    post_id=post_id,
                    user_id=commenter,
                    text=self._random_sentence(random.randint(5, 16)),
                    created_at=now.isoformat() + "Z",
                )
                self.comments[post_id].append(comment)
            self.posts[post_id].comment_count = len(self.comments[post_id])

            # Shares
            share_users = random.sample(user_ids, k=random.randint(0, min(4, len(user_ids))))
            self.shares[post_id].update(share_users)
            self.posts[post_id].share_count = len(self.shares[post_id])

        # Keep latest first
        self.post_ids_ordered.sort(reverse=True)

    def _random_sentence(self, n_words: int) -> str:
        words = ["".join(random.choices(string.ascii_lowercase, k=random.randint(3, 10))) for _ in range(n_words)]
        return " ".join(words).capitalize() + "."

    def get_feed(self, cursor: Optional[str], limit: int) -> Tuple[List[Post], Optional[str]]:
        if limit <= 0:
            return [], None
        ordered = self.post_ids_ordered
        start_index = 0
        if cursor:
            try:
                # cursor is a post_id; start after its index
                start_index = ordered.index(cursor) + 1
            except ValueError:
                start_index = 0
        end_index = min(start_index + limit, len(ordered))
        ids = ordered[start_index:end_index]
        items = [self.posts[i] for i in ids]
        next_cursor = ids[-1] if end_index < len(ordered) and ids else None
        return items, next_cursor

    def get_profile(self, profile_id: str) -> Optional[Profile]:
        return self.profiles.get(profile_id)

    def get_posts_by_author(self, profile_id: str) -> List[Post]:
        ids = [pid for pid in self.post_ids_ordered if self.posts[pid].author_id == profile_id]
        return [self.posts[pid] for pid in ids]

    def toggle_like(self, post_id: str, user_id: str) -> bool:
        liked = False
        users = self.likes.get(post_id)
        if users is None:
            return False
        if user_id in users:
            users.remove(user_id)
            liked = False
        else:
            users.add(user_id)
            liked = True
        self.posts[post_id].like_count = len(users)
        return liked

    def add_comment(self, post_id: str, user_id: str, text: str) -> Optional[Comment]:
        comments = self.comments.get(post_id)
        if comments is None:
            return None
        comment = Comment(
            id=f"c{post_id}-{len(comments)+1}",
            post_id=post_id,
            user_id=user_id,
            text=text,
            created_at=datetime.utcnow().isoformat() + "Z",
        )
        comments.append(comment)
        self.posts[post_id].comment_count = len(comments)
        return comment

    def add_share(self, post_id: str, user_id: str) -> bool:
        users = self.shares.get(post_id)
        if users is None:
            return False
        users.add(user_id)
        self.posts[post_id].share_count = len(users)
        return True


store = InMemoryStore()
store.seed()
