from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, func

from app.database import get_session
from app.models import Movies, MovieActor, MovieGenre

router = APIRouter(prefix="/api/v1", tags=["Movies Filtering  API"])


@router.get("/movies/title/{title}", response_model=dict)
def list_of_movies_by_title(title: str, session: Session = Depends(get_session)):
    query = select(Movies).where(func.lower(Movies.title).contains(title.lower()))
    print(query)
    movies = session.exec(query).all()

    if not movies:
        raise HTTPException(status_code=404, detail="No movies found with this title")

    return {
        "movies": [
            {
                "id": movie.id,
                "title": movie.title,
                "release_year": movie.release_year,
                "director_id": movie.director_id,
            }
            for movie in movies
        ],
        "message": f"{len(movies)} movie(s) found with title '{title}'",
        "status_code": 200,
    }


# list_of_movies_by_release_year
@router.get("/movies/year/{release_year}", response_model=dict)
def list_of_movies_by_release_year(
    release_year: int, session: Session = Depends(get_session)
):
    movies = session.exec(select(Movies).where(Movies.release_year == release_year)).all()

    if not movies:
        raise HTTPException(status_code=404, detail="No movies found for this year")

    return {
        "movies": [
            {
                "id": m.id,
                "title": m.title,
                "release_year": m.release_year,
                "director_id": m.director_id,
            }
            for m in movies
        ],
        "message": f"{len(movies)} movie(s) found from year {release_year}",
        "status_code": 200,
    }


# list_of_movies_by_director
@router.get("/movies/director/{director_id}", response_model=dict)
def list_of_movies_by_director(director_id: int, session: Session = Depends(get_session)):
    movies = session.exec(select(Movies).where(Movies.director_id == director_id)).all()

    if not movies:
        raise HTTPException(status_code=404, detail="No movies found for this director")

    return {
        "movies": [
            {
                "id": m.id,
                "title": m.title,
                "release_year": m.release_year,
                "director_id": m.director_id,
            }
            for m in movies
        ],
        "message": f"{len(movies)} movie(s) found for director ID {director_id}",
        "status_code": 200,
    }


# list_of_movies_by_actor
@router.get("/movies/actor/{actor_id}", response_model=dict)
def list_of_movies_by_actor(actor_id: int, session: Session = Depends(get_session)):
    links = session.exec(select(MovieActor).where(MovieActor.actor_id == actor_id)).all()

    if not links:
        raise HTTPException(status_code=404, detail="No movies found with this actor")

    movies = [session.get(Movies, link.movie_id) for link in links]

    return {
        "movies": [
            {
                "id": m.id,
                "title": m.title,
                "release_year": m.release_year,
                "director_id": m.director_id,
            }
            for m in movies
            if m
        ],
        "message": f"{len(movies)} movie(s) found with actor ID {actor_id}",
        "status_code": 200,
    }


# list_of_movies_by_genre
@router.get("/movies/genre/{genre_id}", response_model=dict)
def list_of_movies_by_genre(genre_id: int, session: Session = Depends(get_session)):
    links = session.exec(select(MovieGenre).where(MovieGenre.genre_id == genre_id)).all()

    if not links:
        raise HTTPException(status_code=404, detail="No movies found with this genre")

    movies = [session.get(Movies, link.movie_id) for link in links]

    return {
        "movies": [
            {
                "id": m.id,
                "title": m.title,
                "release_year": m.release_year,
                "director_id": m.director_id,
            }
            for m in movies
            if m
        ],
        "message": f"{len(movies)} movie(s) found with genre ID {genre_id}",
        "status_code": 200,
    }
