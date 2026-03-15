from fastapi import FastAPI, Depends
from api.route import initial_persona
from api.deps import req_validate

app = FastAPI()

app.include_router(
    initial_persona.router,
    prefix="/api",
    dependencies=[Depends(req_validate)],
)