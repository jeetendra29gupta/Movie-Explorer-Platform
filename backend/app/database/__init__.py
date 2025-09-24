from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///movie-explorer-platform.db"

engine = create_engine(
    DATABASE_URL, echo=False, connect_args={"check_same_thread": False}
)


def get_session():
    with Session(engine) as session:
        yield session
