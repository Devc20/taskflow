from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

# El argumento check_same_thread solo es necesario para SQLite.
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredan todos los modelos de tablas.
Base = declarative_base()


def get_db():
    """Provee una sesión de base de datos por petición y la cierra al terminar.

    FastAPI inyecta esta dependencia en cada endpoint que la necesite.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
