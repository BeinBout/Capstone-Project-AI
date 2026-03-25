from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware
from core.database import create_db_and_tables
from loguru import logger

from api.deps import req_validate
from api.route import initial_persona
from api.route import daily_journal
from api.route import weekly_checkup

@asynccontextmanager
async def startup(app: FastAPI):
    try:
        logger.info("Syncing Database...")
        create_db_and_tables()
        logger.info("✅ Database Sync Done")
    except SQLAlchemyError as e:
        logger.critical(f"DATABASE ERROR: {e}")
        raise e
    except Exception as e:
        logger.error(f"SOMETHING ERROR: {e}")
        raise e

    yield
    logger.info("Stopping Service...")


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

app.include_router(
    daily_journal.router,
    prefix="/api",
    dependencies=[Depends(req_validate)],
)

app.include_router(
    weekly_checkup.router,
    prefix="/api",
    dependencies=[Depends(req_validate)]
)