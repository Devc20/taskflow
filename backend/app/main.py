import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.database import Base, engine
from app.routers import task_router

# Crea las tablas en la base de datos si todavía no existen.
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_title)

# Permite que un frontend en otro origen consuma la API durante el desarrollo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra los endpoints de la API.
app.include_router(task_router.router)

# Sirve el frontend estático. Se monta al final para no tapar las rutas /api.
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
