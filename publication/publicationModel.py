from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from core.db import Base


class PublicationType(Base):
    __tablename__ = 'publication_type'

    id = Column(Integer, primary_key=True, index=True)
    publication_type = Column(String(64))
    paper = relationship("Paper", back_populates='pub_type')
