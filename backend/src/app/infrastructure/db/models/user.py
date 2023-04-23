import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
from infrastructure.db.models.base import Base

class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
