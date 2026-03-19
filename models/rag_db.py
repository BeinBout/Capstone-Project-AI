from datetime import datetime, timezone
from typing import Any, Optional

import sqlalchemy as sa
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP
from sqlmodel import Column, Field, SQLModel


class Rag_db(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(sa_column=Column(sa.Text, nullable=False))
    embedding: list[float] = Field(sa_column=Column(Vector(1536), nullable=False))
    extra_info: dict[str, Any] = Field(
        default_factory=dict, sa_column=Column("extra_info", JSONB)
    )
    source_type: str = Field(max_length=50)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(TIMESTAMP(timezone=True), server_default=sa.func.now()),
    )