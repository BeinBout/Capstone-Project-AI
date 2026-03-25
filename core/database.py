from sqlmodel import create_engine, SQLModel, text
from .config import settings
from models.rag_db import Rag_db # noqa: F401

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
    
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS ix_rag_db_embedding_hnsw 
            ON rag_db USING hnsw (embedding vector_ip_ops)
        """))