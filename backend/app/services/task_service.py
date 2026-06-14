from sqlalchemy.orm import Session

from app.models.task_model import TaskModel
from app.schemas.task_schema import TaskCreate


def list_tasks(db: Session) -> list[TaskModel]:
    """Devuelve todas las tareas existentes."""
    return db.query(TaskModel).all()


def add_task(db: Session, task_data: TaskCreate) -> TaskModel:
    """Crea una tarea nueva y la guarda en la base de datos."""
    new_task = TaskModel(text=task_data.text, is_done=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def mark_task(db: Session, task_id: int, is_done: bool) -> TaskModel | None:
    """Marca una tarea como completada o pendiente.

    Devuelve None si la tarea no existe.
    """
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        return None
    task.is_done = is_done
    db.commit()
    db.refresh(task)
    return task


def remove_task(db: Session, task_id: int) -> bool:
    """Borra una tarea. Devuelve True si existía, False si no."""
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        return False
    db.delete(task)
    db.commit()
    return True
