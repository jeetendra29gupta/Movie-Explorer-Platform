from sqlmodel import SQLModel

from app.database import engine
from app.logger import get_logger
from app.models import Actors
from app.models import Directors
from app.models import Genres
from app.models import MovieActor
from app.models import MovieGenre
from app.models import Movies

logger = get_logger(__name__)


def reset_database_tables():
    """
    Drop the database and tables if it exists.
    And
    Create the database and tables if they do not exist.
    """
    for table in (MovieActor, MovieGenre, Movies, Actors, Directors, Genres):
        logger.info(f"Database Migration for: {table.__table__}")

    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    logger.info("Database created successfully.")


if __name__ == "__main__":
    reset_database_tables()
