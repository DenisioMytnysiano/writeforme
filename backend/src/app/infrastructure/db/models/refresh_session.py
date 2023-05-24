import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from infrastructure.db.models.base import Base


class RefreshSession(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False)
    refresh_token = Column(String, nullable=False)
    fingerprint = Column(String, nullable=False)
