import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_register_login_logs_flow():
    unique = uuid.uuid4().hex[:8]
    username = f"pytest_user_{unique}"
    email = f"pytest_user_{unique}@example.com"
    password = "secret123"

    reg = client.post(
        "/users/register",
        json={"username": username, "email": email, "password": password},
    )
    assert reg.status_code in (200, 201)

    login = client.post(
        "/auth/login",
        data={"username": username, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    add = client.post(
        "/logs/",
        json={"smoked_at": "2026-05-08T15:00:00"},
        headers=headers,
    )
    assert add.status_code == 201
    log_id = add.json()["id"]

    list_resp = client.get("/logs/", headers=headers)
    assert list_resp.status_code == 200
    assert any(item["id"] == log_id for item in list_resp.json())

    delete_resp = client.delete(f"/logs/{log_id}", headers=headers)
    assert delete_resp.status_code == 204