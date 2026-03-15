from sqlmodel import Session, create_engine, SQLModel, text
from .config import settings
from models.rag_db import Rag_db

engine = create_engine(
    settings.DATABASE_URL, 
    echo = True if settings.SERVICE_MODE == "development" else False,   
    pool_size=10,         
    max_overflow=20
)

def create_db_and_tables():
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session

