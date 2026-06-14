# TaskFlow — Gestiona tus tareas pendientes en un solo lugar

Aplicación de gestión de tareas full stack.

- **Backend:** FastAPI + SQLAlchemy + SQLite
- **Frontend:** HTML + CSS + JavaScript (sin frameworks)
- **CI/CD:** Git, GitHub Actions, Docker, Terraform, Jenkins

---

## Arquitectura

El backend está dividido en capas, cada una con una sola responsabilidad:

```
Frontend  ->  Router  ->  Service  ->  Modelo + Schema  ->  Base de datos
            (rutas)    (lógica)     (datos / validación)
```

- **Router** (`task_router.py`): recibe las peticiones HTTP y valida la entrada.
- **Service** (`task_service.py`): contiene la lógica de negocio.
- **Modelo** (`task_model.py`): define la tabla de la base de datos.
- **Schema** (`task_schema.py`): valida los datos que entran y salen.

---

## Cómo correrlo en local

Necesitas Python 3.12 o superior.

```bash
# 1. Entra a la carpeta del backend
cd backend

# 2. Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Arranca el servidor
uvicorn app.main:app --reload
```

Luego abre en el navegador:

- **App:** http://localhost:8000
- **Documentación interactiva de la API:** http://localhost:8000/docs

La documentación en `/docs` la genera FastAPI sola y te deja probar todos
los endpoints sin escribir código.

---

## Endpoints de la API

| Método | Ruta              | Qué hace                       |
|--------|-------------------|--------------------------------|
| GET    | `/api/tasks`      | Lista todas las tareas         |
| POST   | `/api/tasks`      | Crea una tarea                 |
| PUT    | `/api/tasks/{id}` | Marca una tarea completada     |
| DELETE | `/api/tasks/{id}` | Borra una tarea                |

---

## Tests

```bash
cd backend
pytest
```

Los tests usan una base de datos en memoria, así que no tocan tus datos reales.

---

## Docker

```bash
# Construye la imagen (desde la raíz del proyecto)
docker build -f backend/Dockerfile -t taskflow .

# Corre el contenedor
docker run -p 8000:8000 taskflow
```

---

## Orden recomendado para aprender CI/CD

No actives todo de golpe. Sigue este orden:

1. **Git + GitHub** — sube el repo. Aprende `add`, `commit`, `push`, ramas.
2. **GitHub Actions** — ya está listo en `.github/workflows/ci.yml`.
   Corre los tests solo en cada push.
3. **Docker** — conteneriza la app con el `Dockerfile`.
4. **Terraform** — `infrastructure/terraform/` (plantilla de ejemplo).
   Déjalo para cuando entiendas la nube. No lo apliques sin una cuenta AWS.
5. **Jenkins** — `Jenkinsfile` (alternativa a GitHub Actions).
   Solo si una empresa lo usa. No necesitas los dos.

---

## Estructura del proyecto

```
taskflow/
├── .github/workflows/ci.yml      # CI con GitHub Actions
├── backend/
│   ├── app/
│   │   ├── main.py               # Punto de entrada FastAPI
│   │   ├── config.py             # Configuración
│   │   ├── database.py           # Conexión a la BD
│   │   ├── models/task_model.py  # Tabla (SQLAlchemy)
│   │   ├── schemas/task_schema.py# Validación (Pydantic)
│   │   ├── routers/task_router.py# Endpoints
│   │   └── services/task_service.py # Lógica de negocio
│   ├── tests/test_task_router.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
├── infrastructure/terraform/     # Infraestructura como código
├── Jenkinsfile
├── .gitignore
└── README.md
```

---

## Próximos pasos sugeridos

Cuando esto funcione, prueba a:

- Agregar un campo de fecha de vencimiento a las tareas.
- Cambiar SQLite por PostgreSQL (mismo código, otra `DATABASE_URL`).
- Agregar autenticación de usuarios.
- Desplegarlo en la nube (Render o Railway son gratis para empezar).
