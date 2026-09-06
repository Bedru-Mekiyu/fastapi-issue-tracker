import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_timing_middleware():
    response = client.get("/api/v1/health")
    assert "X-Process-Time" in response.headers


def test_issue_crud_lifecycle(tmp_path, monkeypatch):
    # Use a temporary file for storage during tests
    test_data_file = tmp_path / "issues.json"
    import app.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", test_data_file)
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)

    # 1. Initially issues list is empty
    response = client.get("/api/v1/issues")
    assert response.status_code == 200
    assert response.json() == []

    # 2. Create issue
    payload = {
        "title": "Test Issue Title",
        "description": "Test issue description here.",
        "priority": "high"
    }
    create_res = client.post("/api/v1/issues", json=payload)
    assert create_res.status_code == 201
    issue_data = create_res.json()
    assert issue_data["title"] == payload["title"]
    assert issue_data["description"] == payload["description"]
    assert issue_data["priority"] == "high"
    assert issue_data["status"] == "open"
    assert "id" in issue_data
    issue_id = issue_data["id"]

    # 3. Get issue by ID
    get_res = client.get(f"/api/v1/issues/{issue_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == issue_id

    # 4. Update issue
    update_payload = {"status": "in_progress", "priority": "low"}
    update_res = client.put(f"/api/v1/issues/{issue_id}", json=update_payload)
    assert update_res.status_code == 200
    updated = update_res.json()
    assert updated["status"] == "in_progress"
    assert updated["priority"] == "low"

    # 5. Delete issue
    del_res = client.delete(f"/api/v1/issues/{issue_id}")
    assert del_res.status_code == 204

    # 6. Verify non-existent issue gives 404
    get_after_del = client.get(f"/api/v1/issues/{issue_id}")
    assert get_after_del.status_code == 404


def test_get_nonexistent_issue(tmp_path, monkeypatch):
    import app.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "issues.json")
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)

    response = client.get("/api/v1/issues/non-existent-uuid")
    assert response.status_code == 404
