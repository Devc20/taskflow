from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class TaskModel(Base):
    """Representa una fila de la tabla 'tasks' en la base de datos."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    is_done = Column(Boolean, default=False, nullable=False)
