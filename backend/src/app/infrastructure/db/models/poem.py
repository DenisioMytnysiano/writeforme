import uuid

from infrastructure.db.models.base import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Poem(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    owner = relationship("User", back_populates="poems")
