import pytest

from app.main import app
from app.routers.directors import router as directors_router

app.include_router(directors_router)


def test_create_director(client):
    response = client.post("/api/v1/directors", json={"name": "Steven Spielberg"})
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "Steven Spielberg"
    assert data["message"] == "Director created successfully"
    assert "id" in data


def test_list_directors(client):
    client.post("/api/v1/directors", json={"name": "Christopher Nolan"})
    response = client.get("/api/v1/directors")
    data = response.json()
    assert response.status_code == 200
    assert "directors" in data
    assert any(d["name"] == "Christopher Nolan" for d in data["directors"])


def test_get_director(client):
    create_resp = client.post("/api/v1/directors", json={"name": "Quentin Tarantino"})
    director_id = create_resp.json()["id"]

    response = client.get(f"/api/v1/directors/{director_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Quentin Tarantino"


def test_get_nonexistent_director(client):
    response = client.get("/api/v1/directors/9999")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
