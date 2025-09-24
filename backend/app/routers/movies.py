from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Query
from sqlmodel import Session, select

from app.database import get_session
from app.models import Movies, Directors, Actors, Genres, MovieActor, MovieGenre
from app.schemas import MovieCreate

router = APIRouter(prefix="/api/v1", tags=["Movies Routes"])


@router.post("/movies", response_model=dict, status_code=201)
def create_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    # Check director exists if provided
    if movie.director_id:
        director = session.get(Directors, movie.director_id)
        if not director:
            raise HTTPException(status_code=404, detail="Director not found")

    db_movie = Movies(
        title=movie.title,
        release_year=movie.release_year,
        director_id=movie.director_id,
    )
    session.add(db_movie)
    session.commit()
    session.refresh(db_movie)

    # Link actors
    for actor_id in movie.actor_ids:
        actor = session.get(Actors, actor_id)
        if not actor:
            raise HTTPException(
                status_code=404, detail=f"Actor with id {actor_id} not found"
            )
        link = MovieActor(movie_id=db_movie.id, actor_id=actor_id)
        session.add(link)

    # Link genres
    for genre_id in movie.genre_ids:
        genre = session.get(Genres, genre_id)
        if not genre:
            raise HTTPException(
                status_code=404, detail=f"Genre with id {genre_id} not found"
            )
        link = MovieGenre(movie_id=db_movie.id, genre_id=genre_id)
        session.add(link)

    session.commit()
    session.refresh(db_movie)

    return {
        "id": db_movie.id,
        "title": db_movie.title,
        "release_year": db_movie.release_year,
        "director": db_movie.director,
        "actors": db_movie.actors,
        "genres": db_movie.genres,
        "message": "Movie created successfully",
        "status_code": 201,
    }


@router.get("/movies", response_model=dict)
# def list_movies(session: Session = Depends(get_session)):
def list_movies(
    genre_id: Optional[int] = Query(None),
    director_id: Optional[int] = Query(None),
    release_year: Optional[int] = Query(None),
    actor_id: Optional[int] = Query(None),
    session: Session = Depends(get_session),
):
    query = select(Movies)
    if genre_id:
        query = query.join(MovieGenre).where(MovieGenre.genre_id == genre_id)
    if actor_id:
        query = query.join(MovieActor).where(MovieActor.actor_id == actor_id)
    if director_id:
        query = query.where(Movies.director_id == director_id)
    if release_year:
        query = query.where(Movies.release_year == release_year)
    movies = session.exec(query).all()

    result = []
    for movie in movies:
        result.append(
            {
                "id": movie.id,
                "title": movie.title,
                "release_year": movie.release_year,
                "director": movie.director,
                "actors": movie.actors,
                "genres": movie.genres,
            }
        )
    return {
        "movies": result,
        "message": "Movies listed successfully",
        "status_code": 200,
    }


@router.get("/movies/{movie_id}", response_model=dict)
def get_movie(movie_id: int, session: Session = Depends(get_session)):
    movie = session.get(Movies, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return {
        "id": movie.id,
        "title": movie.title,
        "release_year": movie.release_year,
        "director": movie.director,
        "actors": movie.actors,
        "genres": movie.genres,
        "message": "Movie retrieved successfully",
        "status_code": 200,
    }
