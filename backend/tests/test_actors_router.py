import pytest

from app.main import app
from app.routers.actors import router as actors_router

app.include_router(actors_router)


def test_create_actor(client):
    response = client.post("/api/v1/actors", json={"name": "Leonardo Di Caprio"})
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "Leonardo Di Caprio"
    assert data["message"] == "Actor created successfully"
    assert "id" in data


def test_list_actors(client):
    client.post("/api/v1/actors", json={"name": "Meryl Streep"})
    response = client.get("/api/v1/actors")
    data = response.json()
    assert response.status_code == 200
    assert "actors" in data
    assert any(a["name"] == "Meryl Streep" for a in data["actors"])


def test_get_actor(client):
    create_resp = client.post("/api/v1/actors", json={"name": "Tom Hanks"})
    actor_id = create_resp.json()["id"]

    response = client.get(f"/api/v1/actors/{actor_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Tom Hanks"


def test_get_nonexistent_actor(client):
    response = client.get("/api/v1/actors/9999")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
