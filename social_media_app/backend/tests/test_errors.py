from __future__ import annotations
from fastapi.testclient import TestClient

from app.main import app
from app.data import store


class TestErrorBranches:
    """Covers error branches to ensure 100% coverage."""

    def test_feed_author_missing_500(self):
        """When a post's author profile is missing, feed returns 500."""
        client = TestClient(app)
        # Identify first feed post and remove its author profile
        first_page = client.get("/feed", params={"limit": 1}).json()
        if not first_page["items"]:
            return
        author_id = first_page["items"][0]["author"]["id"]
        saved = store.profiles.get(author_id)
        try:
            if saved is not None:
                del store.profiles[author_id]
            resp = client.get("/feed", params={"limit": 1})
            assert resp.status_code == 500
        finally:
            if saved is not None:
                store.profiles[author_id] = saved

    def test_interactions_404s(self):
        """Like/Comment/Share return 404 for missing post."""
        client = TestClient(app)
        for path in ["like", "comment", "share"]:
            resp = client.post(f"/posts/does-not-exist/{path}", json={"user_id": "u01", "text": "x"})
            assert resp.status_code == 404

    def test_comment_400_when_comments_map_missing(self):
        """Comment returns 400 if comments map is missing for post."""
        client = TestClient(app)
        post_id = "p010"
        # Ensure post exists then remove comments map
        assert post_id in store.posts
        saved = store.comments.get(post_id)
        try:
            if post_id in store.comments:
                del store.comments[post_id]
            resp = client.post(f"/posts/{post_id}/comment", json={"user_id": "u01", "text": "hey"})
            assert resp.status_code == 400
        finally:
            if saved is not None:
                store.comments[post_id] = saved

    def test_share_400_when_shares_map_missing(self):
        """Share returns 400 if shares map is missing for post."""
        client = TestClient(app)
        post_id = "p011"
        assert post_id in store.posts
        saved = store.shares.get(post_id)
        try:
            if post_id in store.shares:
                del store.shares[post_id]
            resp = client.post(f"/posts/{post_id}/share", json={"user_id": "u02"})
            assert resp.status_code == 400
        finally:
            if saved is not None:
                store.shares[post_id] = saved


class TestDataBranches:
    """Direct tests against data store for edge cases."""

    def test_get_feed_limit_zero(self):
        """get_feed returns empty when limit <= 0."""
        items, cursor = store.get_feed(cursor=None, limit=0)
        assert items == []
        assert cursor is None

    def test_get_feed_invalid_cursor(self):
        """Invalid cursor gracefully starts from beginning."""
        items, cursor = store.get_feed(cursor="not-a-valid-id", limit=5)
        assert len(items) <= 5

    def test_toggle_like_when_likes_map_missing(self):
        """toggle_like returns False if likes map missing."""
        post_id = "p012"
        assert post_id in store.posts
        saved = store.likes.get(post_id)
        try:
            if post_id in store.likes:
                del store.likes[post_id]
            result = store.toggle_like(post_id, "u01")
            assert result is False
        finally:
            if saved is not None:
                store.likes[post_id] = saved

    def test_add_comment_when_comments_map_missing(self):
        """add_comment returns None if comments map missing."""
        post_id = "p013"
        saved = store.comments.get(post_id)
        try:
            if post_id in store.comments:
                del store.comments[post_id]
            result = store.add_comment(post_id, "u02", "hello")
            assert result is None
        finally:
            if saved is not None:
                store.comments[post_id] = saved

    def test_add_share_when_shares_map_missing(self):
        """add_share returns False if shares map missing."""
        post_id = "p014"
        saved = store.shares.get(post_id)
        try:
            if post_id in store.shares:
                del store.shares[post_id]
            ok = store.add_share(post_id, "u03")
            assert ok is False
        finally:
            if saved is not None:
                store.shares[post_id] = saved
