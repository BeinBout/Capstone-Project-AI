from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware

from api.deps import req_validate
from api.route import initial_persona
from core.database import create_db_and_tables


@asynccontextmanager
async def startup(app: FastAPI):
    try:
        print("Syncing Database...")
        create_db_and_tables()
        print("✅ Database Sync Done")
    except SQLAlchemyError as e:
        print(f"DATABASE ERROR: {e}")
        raise e
    except Exception as e:
        print(f"SOMETHING ERROR: {e}")
        raise e

    yield
    print("Stopping Service...")


app = FastAPI(lifespan=startup)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    initial_persona.router,
    prefix="/api",
    dependencies=[Depends(req_validate)],
)