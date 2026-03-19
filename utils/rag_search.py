from sqlmodel import Session, select, Float

from core.database import engine
from models.rag_db import Rag_db


async def rag_search(query_vector: list[float], top_k: int = 5, threshold: float = 0.5):
    with Session(engine) as session:
        distance_col = Rag_db.embedding.op("<=>", return_type=Float)(query_vector) # type: ignore[attr-defined]
        query = (
            select(Rag_db, distance_col.label("distance"))
            .where(distance_col < threshold)
            .order_by("distance")
            .limit(top_k)
        )
        return session.exec(query).all()

