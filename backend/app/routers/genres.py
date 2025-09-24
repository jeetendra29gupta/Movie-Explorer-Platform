from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session
from sqlmodel import select

from app.database import get_session
from app.models import Genres
from app.schemas import GenreCreate

router = APIRouter(prefix="/api/v1", tags=["Genres Routes"])


@router.post("/genres", response_model=dict, status_code=201)
def create_genre(genre: GenreCreate, session: Session = Depends(get_session)):
    db_genre = Genres(name=genre.name)
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)
    return {
        "id": db_genre.id,
        "name": db_genre.name,
        "message": "Genre created successfully",
        "status_code": 201,
    }


@router.get("/genres", response_model=dict)
def list_genres(session: Session = Depends(get_session)):
    genres = session.exec(select(Genres)).all()
    return {
        "genres": [
            {
                "id": genre.id,
                "name": genre.name,
            }
            for genre in genres
        ],
        "message": "Genres listed successfully",
        "status_code": 200,
    }


@router.get("/genres/{genre_id}", response_model=dict)
def get_genre(genre_id: int, session: Session = Depends(get_session)):
    genre = session.get(Genres, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return {
        "id": genre.id,
        "name": genre.name,
        "message": "Genre retrieved successfully",
        "status_code": 200,
    }
