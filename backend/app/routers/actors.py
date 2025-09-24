from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlmodel import Session
from sqlmodel import select

from app.database import get_session
from app.models import Actors
from app.schemas import ActorCreate

router = APIRouter(prefix="/api/v1", tags=["Actors Routes"])


@router.post("/actors", response_model=dict, status_code=201)
def create_actor(actor: ActorCreate, session: Session = Depends(get_session)):
    db_actor = Actors(name=actor.name)
    session.add(db_actor)
    session.commit()
    session.refresh(db_actor)
    return {
        "id": db_actor.id,
        "name": db_actor.name,
        "message": "Actor created successfully",
        "status_code": 201,
    }


@router.get("/actors", response_model=dict)
def list_actors(session: Session = Depends(get_session)):
    actors = session.exec(select(Actors)).all()
    return {
        "actors": [
            {
                "id": actor.id,
                "name": actor.name,
            }
            for actor in actors
        ],
        "message": "Actors listed successfully",
        "status_code": 200,
    }


@router.get("/actors/{actor_id}", response_model=dict)
def get_actor(actor_id: int, session: Session = Depends(get_session)):
    actor = session.get(Actors, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {
        "id": actor.id,
        "name": actor.name,
        "message": "Actor retrieved successfully",
        "status_code": 200,
    }
