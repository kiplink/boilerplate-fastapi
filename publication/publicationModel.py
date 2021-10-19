from sqlalchemy import Column, String, Integer

from core.db import Base


class PublicationType(Base):
    __tablename__ = 'publication_type'

    id = Column(Integer, primary_key=True, index=True)
    publication_type = Column(String(64))
