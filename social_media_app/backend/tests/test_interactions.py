from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app


class TestInteractions:
    """Tests for like, comment, share endpoints."""

    def test_like_toggle(self):
        """Toggles like and returns updated counts."""
        client = TestClient(app)
        post_id = "p001"
        r1 = client.post(f"/posts/{post_id}/like", json={"user_id": "u99"})
        assert r1.status_code == 200
        data1 = r1.json()
        assert "post" in data1 and "liked_by_user" in data1
        liked_state = data1["liked_by_user"]
        r2 = client.post(f"/posts/{post_id}/like", json={"user_id": "u99"})
        assert r2.status_code == 200
        data2 = r2.json()
        assert data2["liked_by_user"] != liked_state

    def test_comment(self):
        """Adds a comment and returns it with updated post."""
        client = TestClient(app)
        post_id = "p002"
        r = client.post(f"/posts/{post_id}/comment", json={"user_id": "u01", "text": "Nice post!"})
        assert r.status_code == 200
        data = r.json()
        assert data["new_comment"]["text"] == "Nice post!"
        assert data["post"]["comment_count"] >= 1

    def test_share(self):
        """Shares a post and increments share count."""
        client = TestClient(app)
        post_id = "p003"
        r = client.post(f"/posts/{post_id}/share", json={"user_id": "u02"})
        assert r.status_code == 200
        data = r.json()
        assert "post" in data

    def test_list_comments_and_404(self):
        """Lists comments for a post and returns 404 for missing post."""
        client = TestClient(app)
        post_id = "p003"
        ok = client.get(f"/posts/{post_id}/comments")
        assert ok.status_code == 200
        missing = client.get("/posts/does-not-exist/comments")
        assert missing.status_code == 404
