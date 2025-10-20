from __future__ import annotations
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .telemetry import init_telemetry
from .routers.feed import router as feed_router
from .routers.profiles import router as profiles_router
from .routers.interactions import router as interactions_router


app = FastAPI(title="Social Media Backend", version="0.1.0")

# CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_telemetry(app)

app.include_router(feed_router)
app.include_router(profiles_router)
app.include_router(interactions_router)


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}
