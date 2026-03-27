from sqlmodel import create_engine, SQLModel, text
from .config import settings
from loguru import logger
from models.rag_db import Rag_db # noqa: F401

engine = create_engine(
    settings.DATABASE_URL, 
    echo = True if settings.SERVICE_MODE == "development" else False,   
    pool_size=10,         
    max_overflow=20
)

def create_db_and_tables():
    logger.info("DB: Enabling vector extension and sync all DB...")
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    SQLModel.metadata.create_all(bind=engine)
    logger.info("DB: Vector extension enabled, all DB sync!")
    
    logger.info("DB: Creating HNSW Index...")
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS ix_rag_db_embedding_hnsw 
            ON rag_db USING hnsw (embedding vector_ip_ops)
            WITH (m = 16, ef_construction = 64)
        """))
    logger.info("DB :Indexing HNSW Done!")
    