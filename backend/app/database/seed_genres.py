from sqlmodel import Session, select

from app.database import engine
from app.logger import get_logger
from app.models import Genres

logger = get_logger(__name__)
genres_list = [
    "Action",
    "Comedy",
    "Drama",
    "Horror",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "Documentary",
    "Fantasy",
    "Animation",
]


def seed_genres():
    with Session(engine) as session:
        for name in genres_list:
            existing = session.exec(select(Genres).where(Genres.name == name)).first()
            if not existing:
                session.add(Genres(name=name))
        session.commit()
    logger.info("Seeded 10 genres.")


if __name__ == "__main__":
    seed_genres()
