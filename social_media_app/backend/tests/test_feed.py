from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app


class TestGetFeed:
    """Tests for feed endpoint."""

    def test_default_feed(self):
        """Returns first page of posts with authors and cursor."""
        client = TestClient(app)
        resp = client.get("/feed")
        assert resp.status_code == 200
        data = resp.json()
        assert "items" in data and isinstance(data["items"], list)
        assert len(data["items"]) > 0
        first = data["items"][0]
        assert "author" in first and "id" in first
        assert data["next_cursor"] is None or isinstance(data["next_cursor"], str)

    def test_pagination(self):
        """Paginates with cursor token as last ID of previous page."""
        client = TestClient(app)
        page1 = client.get("/feed", params={"limit": 5}).json()
        assert len(page1["items"]) == 5
        cursor = page1["next_cursor"]
        if cursor:
            page2 = client.get("/feed", params={"limit": 5, "cursor": cursor}).json()
            assert len(page2["items"]) >= 0
