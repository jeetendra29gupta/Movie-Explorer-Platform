from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class MovieActor(SQLModel, table=True):
    movie_id: int = Field(default=None, foreign_key="movies.id", primary_key=True)
    actor_id: int = Field(default=None, foreign_key="actors.id", primary_key=True)


class MovieGenre(SQLModel, table=True):
    movie_id: int = Field(default=None, foreign_key="movies.id", primary_key=True)
    genre_id: int = Field(default=None, foreign_key="genres.id", primary_key=True)


class Directors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    movies: List["Movies"] = Relationship(back_populates="director")


class Genres(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    movies: List["Movies"] = Relationship(back_populates="genres", link_model=MovieGenre)


class Actors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    movies: List["Movies"] = Relationship(back_populates="actors", link_model=MovieActor)


class Movies(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    release_year: int
    director_id: Optional[int] = Field(default=None, foreign_key="directors.id")

    director: Optional[Directors] = Relationship(back_populates="movies")
    actors: List["Actors"] = Relationship(back_populates="movies", link_model=MovieActor)
    genres: List["Genres"] = Relationship(back_populates="movies", link_model=MovieGenre)
