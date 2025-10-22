from fastapi import FastAPI
from src.api.spy_cats_api import router as router_cats
from src.api.missions_api import router as router_missions
from src.api.targets_api import router as router_targets

app = FastAPI(title="Spy Cats")
app.include_router(router_cats, tags=["cats"])
app.include_router(router_missions, tags=["missions"])
app.include_router(router_targets, tags=["targets"])