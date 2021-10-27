import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
from core.db import Base
from sqlalchemy.orm import relationship


class Paper(Base):
    __tablename__ = 'paper'
    paper_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    publication_type = Column(Integer, ForeignKey("publication_type.id"))
    title = Column(String(255))
    abstract = Column(Text, nullable=True)
    publication_year = Column(Integer)
    doi = Column(String(255), nullable=True)
    publisher = Column(String(64), nullable=True)
    createdat = Column(DateTime, default=datetime.datetime.now())
    updatedat = Column(DateTime, default=datetime.datetime.now())
    pub_type = relationship("PublicationType", back_populates='paper')
    authorship = relationship("Authorship", back_populates='paper')

