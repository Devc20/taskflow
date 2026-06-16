import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

# Base de datos en memoria, aislada y exclusiva para los tests.
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def reset_database():
    """Crea tablas limpias antes de cada test y las borra al terminar."""
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=test_engine)
    app.dependency_overrides.clear()


client = TestClient(app)


def test_create_and_list_task():
    response = client.post("/api/tasks", json={"text": "Aprender FastAPI"})
    assert response.status_code == 201

    created = response.json()
    assert created["text"] == "Aprender FastAPI"
    assert created["is_done"] is False

    list_response = client.get("/api/tasks")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1


def test_update_task():
    created = client.post("/api/tasks", json={"text": "Tarea"}).json()
    response = client.put(f"/api/tasks/{created['id']}", json={"is_done": True})
    assert response.status_code == 200
    assert response.json()["is_done"] is True


def test_delete_task():
    created = client.post("/api/tasks", json={"text": "Borrar esto"}).json()
    response = client.delete(f"/api/tasks/{created['id']}")
    assert response.status_code == 204

    list_response = client.get("/api/tasks")
    assert len(list_response.json()) == 0


def test_update_missing_task_returns_404():
    response = client.put("/api/tasks/999", json={"is_done": True})
    assert response.status_code == 404
