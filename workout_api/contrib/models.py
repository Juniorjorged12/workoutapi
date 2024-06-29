from datetime import datetime
from uuid import uuid4
from sqlalchemy import UUID, DateTime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), defult=uuid4, nullable = False)
