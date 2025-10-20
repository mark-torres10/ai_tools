from __future__ import annotations
from fastapi.testclient import TestClient
from app.main import app


class TestGetProfile:
    """Tests for profile endpoint."""

    def test_get_profile(self):
        """Returns a profile and their posts."""
        client = TestClient(app)
        # Seed ensures u01 exists
        resp = client.get("/profiles/u01")
        assert resp.status_code == 200
        data = resp.json()
        assert data["profile"]["id"] == "u01"
        assert isinstance(data["posts"], list)

    def test_missing_profile(self):
        """Returns 404 for missing profile."""
        client = TestClient(app)
        resp = client.get("/profiles/does-not-exist")
        assert resp.status_code == 404
