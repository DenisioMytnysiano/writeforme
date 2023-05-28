import uuid

from infrastructure.db.models.base import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    poems = relationship("Poem", back_populates="owner")
