import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_get_user():
    resp = requests.get(f"{BASE}/users/2")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 2
    assert "@" in data["email"]


def test_create_user():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = requests.post(f"{BASE}/posts", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "foo"
    assert "id" in body


def test_update_user():
    payload = {"id": 1, "title": "baz", "body": "updated", "userId": 1}
    resp = requests.put(f"{BASE}/posts/1", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["title"] == "baz"
