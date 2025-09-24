from sqlmodel import Session, select

from app.database import engine
from app.logger import get_logger
from app.models import Directors

logger = get_logger(__name__)

directors_list = [
    "Steven Spielberg",
    "Christopher Nolan",
    "Quentin Tarantino",
    "Martin Scorsese",
    "Ridley Scott",
    "James Cameron",
    "Alfred Hitchcock",
    "Stanley Kubrick",
    "Peter Jackson",
    "Guillermo del Toro",
]


def seed_directors():
    with Session(engine) as session:
        for name in directors_list:
            existing = session.exec(
                select(Directors).where(Directors.name == name)
            ).first()
            if not existing:
                session.add(Directors(name=name))
        session.commit()
    logger.info("Seeded 10 directors.")


if __name__ == "__main__":
    seed_directors()
