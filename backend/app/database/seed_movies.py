from sqlmodel import Session, select

from app.database import engine
from app.logger import get_logger
from app.models import Movies, Directors, Actors, Genres, MovieActor, MovieGenre

logger = get_logger(__name__)

movies_list = [
    {
        "title": "Inception",
        "release_year": 2010,
        "director_name": "Christopher Nolan",
        "actor_names": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genre_names": ["Action", "Sci-Fi"],
    },
    {
        "title": "The Dark Knight",
        "release_year": 2008,
        "director_name": "Christopher Nolan",
        "actor_names": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "genre_names": ["Action", "Drama"],
    },
    {
        "title": "Pulp Fiction",
        "release_year": 1994,
        "director_name": "Quentin Tarantino",
        "actor_names": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
        "genre_names": ["Crime", "Drama"],
    },
    {
        "title": "The Godfather",
        "release_year": 1972,
        "director_name": "Francis Ford Coppola",
        "actor_names": ["Marlon Brando", "Al Pacino", "James Caan"],
        "genre_names": ["Crime", "Drama"],
    },
    {
        "title": "Fight Club",
        "release_year": 1999,
        "director_name": "David Fincher",
        "actor_names": ["Brad Pitt", "Edward Norton"],
        "genre_names": ["Drama"],
    },
    {
        "title": "Forrest Gump",
        "release_year": 1994,
        "director_name": "Robert Zemeckis",
        "actor_names": ["Tom Hanks", "Robin Wright"],
        "genre_names": ["Drama", "Romance"],
    },
    {
        "title": "The Matrix",
        "release_year": 1999,
        "director_name": "The Wachowskis",
        "actor_names": ["Keanu Reeves", "Laurence Fishburne"],
        "genre_names": ["Action", "Sci-Fi"],
    },
    {
        "title": "Gladiator",
        "release_year": 2000,
        "director_name": "Ridley Scott",
        "actor_names": ["Russell Crowe", "Joaquin Phoenix"],
        "genre_names": ["Action", "Drama"],
    },
    {
        "title": "Titanic",
        "release_year": 1997,
        "director_name": "James Cameron",
        "actor_names": ["Leonardo DiCaprio", "Kate Winslet"],
        "genre_names": ["Drama", "Romance"],
    },
    {
        "title": "The Shawshank Redemption",
        "release_year": 1994,
        "director_name": "Frank Darabont",
        "actor_names": ["Tim Robbins", "Morgan Freeman"],
        "genre_names": ["Drama"],
    },
]


def seed_movies():
    with Session(engine) as session:
        for movie_data in movies_list:
            # Get director
            director = session.exec(
                select(Directors).where(Directors.name == movie_data["director_name"])
            ).first()
            if not director:
                director = Directors(name=movie_data["director_name"])
                session.add(director)
                session.commit()
                session.refresh(director)

            # Create movie
            movie = Movies(
                title=movie_data["title"],
                release_year=movie_data["release_year"],
                director_id=director.id,
            )
            session.add(movie)
            session.commit()  # to assign movie.id
            session.refresh(movie)

            # Link actors
            for actor_name in movie_data["actor_names"]:
                actor = session.exec(
                    select(Actors).where(Actors.name == actor_name)
                ).first()
                if not actor:
                    actor = Actors(name=actor_name)
                    session.add(actor)
                    session.commit()
                    session.refresh(actor)
                link = MovieActor(movie_id=movie.id, actor_id=actor.id)
                session.add(link)

            # Link genres
            for genre_name in movie_data["genre_names"]:
                genre = session.exec(
                    select(Genres).where(Genres.name == genre_name)
                ).first()
                if not genre:
                    genre = Genres(name=genre_name)
                    session.add(genre)
                    session.commit()
                    session.refresh(genre)
                link = MovieGenre(movie_id=movie.id, genre_id=genre.id)
                session.add(link)

            session.commit()

    logger.info("Seeded 10 movies successfully.")


if __name__ == "__main__":
    seed_movies()
