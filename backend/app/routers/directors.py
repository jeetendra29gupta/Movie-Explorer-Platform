from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session
from sqlmodel import select

from app.database import get_session
from app.models import Directors
from app.schemas import DirectorCreate

router = APIRouter(prefix="/api/v1", tags=["Directors Routes"])


@router.post("/directors", response_model=dict, status_code=201)
def create_director(director: DirectorCreate, session: Session = Depends(get_session)):
    db_director = Directors(name=director.name)
    session.add(db_director)
    session.commit()
    session.refresh(db_director)
    return {
        "id": db_director.id,
        "name": db_director.name,
        "message": "Director created successfully",
        "status_code": 201,
    }


@router.get("/directors", response_model=dict)
def list_directors(session: Session = Depends(get_session)):
    directors = session.exec(select(Directors)).all()
    return {
        "directors": [
            {
                "id": director.id,
                "name": director.name,
            }
            for director in directors
        ],
        "message": "Directors listed successfully",
        "status_code": 200,
    }


@router.get("/directors/{director_id}", response_model=dict)
def get_director(director_id: int, session: Session = Depends(get_session)):
    director = session.get(Directors, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return {
        "id": director.id,
        "name": director.name,
        "message": "Director retrieved successfully",
        "status_code": 200,
    }
