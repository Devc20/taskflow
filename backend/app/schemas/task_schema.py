from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Campos compartidos por las distintas representaciones de una tarea."""

    text: str = Field(..., min_length=1, description="Texto de la tarea")


class TaskCreate(TaskBase):
    """Datos que el cliente envía al crear una tarea."""


class TaskUpdate(BaseModel):
    """Datos que el cliente envía al actualizar una tarea."""

    is_done: bool


class TaskResponse(TaskBase):
    """Datos que el servidor devuelve al cliente."""

    id: int
    is_done: bool

    # Permite construir el schema directamente desde un objeto SQLAlchemy.
    model_config = {"from_attributes": True}
