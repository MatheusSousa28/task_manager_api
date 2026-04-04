from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.routers.auth import router as auth_router
from app.routers.tasks import router as tasks_router
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)


@app.get("/")
def healthcheck():
    return {"status": "ok", "app": settings.app_name}


app.include_router(users_router)
app.include_router(tasks_router)
app.include_router(auth_router)
