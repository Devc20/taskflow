import os


class Settings:
    """Configuración central de la aplicación.

    Lee las variables de entorno y provee valores por defecto.
    En producción, DATABASE_URL apuntaría a PostgreSQL.
    """

    app_title: str = "TaskFlow API"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./taskflow.db")


settings = Settings()
