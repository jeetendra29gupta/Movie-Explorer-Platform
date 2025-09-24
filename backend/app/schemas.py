from typing import List
from typing import Optional

from sqlmodel import SQLModel


# ----- DIRECTORS -----
class DirectorCreate(SQLModel):
    name: str


# ----- GENRES -----
class GenreCreate(SQLModel):
    name: str


# ----- ACTORS -----


class ActorCreate(SQLModel):
    name: str


# ----- MOVIES -----
class MovieCreate(SQLModel):
    title: str
    release_year: int
    director_id: Optional[int]
    actor_ids: Optional[List[int]] = []
    genre_ids: Optional[List[int]] = []
