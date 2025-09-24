import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database_migration import reset_database_tables
from app.database.seed_actors import seed_actors
from app.database.seed_directors import seed_directors
from app.database.seed_genres import seed_genres
from app.database.seed_movies import seed_movies
from app.routers import actors
from app.routers import directors
from app.routers import genres
from app.routers import movies

app = FastAPI(
    title="Movie Explorer API",
    description="A RESTful API for exploring movies, directors, actors, and genres.",
    version="1.0.0",
)
reset_database_tables()

origins = [
    "http://localhost:9191",
    "http://127.0.0.1:9191",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/", tags=["Health Check"])
def root():
    """Welcome endpoint for the Movie Explorer API."""
    return {"message": "Welcome to Movie Explorer API"}


app.include_router(directors.router)
seed_directors()
app.include_router(genres.router)
seed_genres()
app.include_router(actors.router)
seed_actors()
app.include_router(movies.router)
seed_movies()


@app.get("/health", tags=["Health Check"])
async def health_check():
    """Health check endpoint to verify that the API is running."""
    return {"status": "healthy"}


if __name__ == "__main__":
    # uvicorn app.main:app --reload --host '0.0.0.0' --port 8181
    uvicorn.run("app.main:app", host="0.0.0.0", port=8181, reload=True)
