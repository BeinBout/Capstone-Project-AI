from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from api.route import initial_persona
from api.deps import req_validate
from core.database import create_db_and_tables
from sqlalchemy.exc import SQLAlchemyError

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

app.include_router(
    initial_persona.router,
    prefix="/api",
    dependencies=[Depends(req_validate)],
)