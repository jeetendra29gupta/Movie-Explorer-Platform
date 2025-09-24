import pytest
from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, create_engine, Session

from app.database import get_session
from app.main import app

SQLITE_TEST_DB = "sqlite:///:memory:"

engine = create_engine(
    SQLITE_TEST_DB,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def override_get_session():
    """Dependency override to provide a test database session."""
    with Session(engine) as session:
        yield session


# Apply the dependency override to the main app
app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(name="client")
def client_fixture():
    """Pytest fixture to create and tear down the database for each test."""
    # print("Tables to create:", SQLModel.metadata.tables.keys())
    SQLModel.metadata.create_all(engine)
    yield TestClient(app)
    SQLModel.metadata.drop_all(engine)
