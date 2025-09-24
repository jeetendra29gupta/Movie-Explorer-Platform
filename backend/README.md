# Movie Explorer Platform

## Features

- **RESTful API**: Built on FastAPI for high performance and easy development.
- **Movie Database**: Manage movies with details such as title, year, genres, director, and actors.
- **Actors/Directors/Genres**: CRUD operations for all related entities.
- **Automatic Seeding**: Populates database with demo data for movies, actors, directors, and genres.
- **Test Coverage**: Includes pytest-based tests for API endpoints.
- **Logging**: Structured logging to file for debugging and auditing.
- **Database Migration**: Auto-reset and migrations for clean development.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pytest](https://docs.pytest.org/)

## Project Structure

```
app/
│
├── main.py                  # FastAPI entry point, router and seed logic
├── logger.py                # Logging configuration
├── schemas.py               # Pydantic/SQLModel schemas for validation
├── models.py                # SQLModel models (not shown, but referenced)
├── database/
│   ├── __init__.py          # Database connection setup
│   ├── database_migration.py# Reset/migrate database tables
│   ├── seed_actors.py       # Seed demo actors
│   ├── seed_directors.py    # Seed demo directors
│   ├── seed_genres.py       # Seed demo genres
│   └── seed_movies.py       # Seed demo movies
├── routers/
│    ├── actors.py            # Actor CRUD routes
│    ├── directors.py         # Director CRUD routes
│    ├── genres.py            # Genre CRUD routes
│    └── movies.py            # Movie CRUD routes
│
├── tests/
│   ├── conftest.py              # Pytest fixtures and test DB setup
│   ├── test_root.py             # Health-check endpoint test
│   ├── test_actors_router.py    # Actor API tests
│   ├── test_directors_router.py # Director API tests
│   ├── test_genres_router.py    # Genre API tests
│   └── test_movies_router.py    # Movie API tests (assumed)
└──
```

---

### Example API Endpoints

- **GET /**  
  Health check & welcome:  
  `GET http://localhost:8181/` → `{ "message": "Welcome to Movie Explorer API" }`

- **Actors**
    - List actors: `GET /api/v1/actors`
    - Get actor by ID: `GET /api/v1/actors/{actor_id}`
    - Add actor: `POST /api/v1/actors` (JSON: `{ "name": "Actor Name" }`)

- **Directors**
    - List directors: `GET /api/v1/directors`
    - Get director by ID: `GET /api/v1/directors/{director_id}`
    - Add director: `POST /api/v1/directors` (JSON: `{ "name": "Director Name" }`)

- **Genres**
    - List genres: `GET /api/v1/genres`
    - Get genre by ID: `GET /api/v1/genres/{genre_id}`
    - Add genre: `POST /api/v1/genres` (JSON: `{ "name": "Genre Name" }`)

- **Movies**
    - List movies: `GET /api/v1/movies`
    - Get movie by ID: `GET /api/v1/movies/{movie_id}`
    - Add movie: `POST /api/v1/movies`
      ```json
      {
        "title": "Inception",
        "release_year": 2010,
        "director_id": 1,
        "actor_ids": [1, 2, 3],
        "genre_ids": [1, 2]
      }
      ```

---