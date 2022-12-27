from fastapi import FastAPI
from project.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()
    app.celery_app = create_celery()

    from project.users.users import users_router
    app.include_router(users_router)

    @app.get("/ping")
    async def ping():
        return {"message": "pong"}

    return app
