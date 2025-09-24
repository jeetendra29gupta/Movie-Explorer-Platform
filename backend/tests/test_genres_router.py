import pytest

from app.main import app
from app.routers.genres import router as genres_router

app.include_router(genres_router)


def test_create_genre(client):
    response = client.post("/api/v1/genres", json={"name": "Action"})
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "Action"
    assert data["message"] == "Genre created successfully"
    assert "id" in data


def test_list_genres(client):
    client.post("/api/v1/genres", json={"name": "Comedy"})
    response = client.get("/api/v1/genres")
    data = response.json()
    assert response.status_code == 200
    assert "genres" in data
    assert any(g["name"] == "Comedy" for g in data["genres"])


def test_get_genre(client):
    create_resp = client.post("/api/v1/genres", json={"name": "Drama"})
    genre_id = create_resp.json()["id"]

    response = client.get(f"/api/v1/genres/{genre_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Drama"


def test_get_nonexistent_genre(client):
    response = client.get("/api/v1/genres/9999")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
