from fastapi import FastAPI
from src.api.spy_cats_api import router

app = FastAPI(title="Spy Cats")
app.include_router(router, tags=["spy"])