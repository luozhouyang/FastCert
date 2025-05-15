from fastapi import FastAPI

from .routes.certs import router as certs_router
from .routes.challenges import router as challenges_router
from .routes.health import router as health_router

app = FastAPI()

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(certs_router, prefix="/api/v1", tags=["certificates"])
app.include_router(challenges_router, prefix="/api/v1", tags=["challenges"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
