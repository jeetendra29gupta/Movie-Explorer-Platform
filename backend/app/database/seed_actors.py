from sqlmodel import Session, select

from app.database import engine
from app.logger import get_logger
from app.models import Actors

logger = get_logger(__name__)

actors_list = [
    "Leonardo DiCaprio",
    "Meryl Streep",
    "Tom Hanks",
    "Natalie Portman",
    "Denzel Washington",
    "Scarlett Johansson",
    "Morgan Freeman",
    "Emma Stone",
    "Brad Pitt",
    "Jennifer Lawrence",
]


def seed_actors():
    with Session(engine) as session:
        for name in actors_list:
            existing = session.exec(select(Actors).where(Actors.name == name)).first()
            if not existing:
                session.add(Actors(name=name))
        session.commit()
    logger.info("Seeded 10 actors.")


if __name__ == "__main__":
    seed_actors()
