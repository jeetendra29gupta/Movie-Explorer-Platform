import pytest

from app.main import app
from app.routers.actors import router as actors_router
from app.routers.directors import router as directors_router
from app.routers.genres import router as genres_router
from app.routers.movies import router as movies_router

app.include_router(movies_router)
app.include_router(directors_router)
app.include_router(actors_router)
app.include_router(genres_router)


def create_dependencies(client):
    """Helper to create a director, two actors, and two genres for testing movies."""
    director = client.post("/api/v1/directors", json={"name": "Christopher Nolan"}).json()
    actor1 = client.post("/api/v1/actors", json={"name": "Leonardo DiCaprio"}).json()
    actor2 = client.post("/api/v1/actors", json={"name": "Joseph Gordon-Levitt"}).json()
    genre1 = client.post("/api/v1/genres", json={"name": "Sci-Fi"}).json()
    genre2 = client.post("/api/v1/genres", json={"name": "Action"}).json()

    return {
        "director": director,
        "actors": [actor1, actor2],
        "genres": [genre1, genre2],
    }


def test_create_movie(client):
    deps = create_dependencies(client)
    response = client.post(
        "/api/v1/movies",
        json={
            "title": "Inception",
            "release_year": 2010,
            "director_id": deps["director"]["id"],
            "actor_ids": [a["id"] for a in deps["actors"]],
            "genre_ids": [g["id"] for g in deps["genres"]],
        },
    )
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "Inception"
    assert data["release_year"] == 2010
    assert data["director"]["name"] == "Christopher Nolan"
    assert len(data["actors"]) == 2
    assert len(data["genres"]) == 2
    assert data["message"] == "Movie created successfully"


def test_list_movies_filter_by_genre(client):
    deps = create_dependencies(client)
    client.post(
        "/api/v1/movies",
        json={
            "title": "Interstellar",
            "release_year": 2014,
            "director_id": deps["director"]["id"],
            "actor_ids": [deps["actors"][0]["id"]],
            "genre_ids": [deps["genres"][0]["id"]],
        },
    )

    response = client.get(f"/api/v1/movies?genre_id={deps['genres'][0]['id']}")
    data = response.json()
    assert response.status_code == 200
    assert any(movie["title"] == "Interstellar" for movie in data["movies"])


def test_list_movies_filter_by_actor(client):
    deps = create_dependencies(client)
    client.post(
        "/api/v1/movies",
        json={
            "title": "The Dark Knight",
            "release_year": 2008,
            "director_id": deps["director"]["id"],
            "actor_ids": [deps["actors"][1]["id"]],
            "genre_ids": [deps["genres"][1]["id"]],
        },
    )

    response = client.get(f"/api/v1/movies?actor_id={deps['actors'][1]['id']}")
    data = response.json()
    assert response.status_code == 200
    assert any(movie["title"] == "The Dark Knight" for movie in data["movies"])


def test_get_movie(client):
    deps = create_dependencies(client)
    create_resp = client.post(
        "/api/v1/movies",
        json={
            "title": "Tenet",
            "release_year": 2020,
            "director_id": deps["director"]["id"],
            "actor_ids": [deps["actors"][0]["id"]],
            "genre_ids": [deps["genres"][1]["id"]],
        },
    )
    movie_id = create_resp.json()["id"]

    response = client.get(f"/api/v1/movies/{movie_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Tenet"
    assert data["release_year"] == 2020
    assert data["director"]["name"] == "Christopher Nolan"


def test_get_nonexistent_movie(client):
    response = client.get("/api/v1/movies/9999")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
