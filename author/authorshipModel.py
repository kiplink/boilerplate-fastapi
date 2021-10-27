from sqlalchemy import Column, Integer, ForeignKey
from core.db import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Authorship(Base):
    __tablename__ = 'authorship'
    authorship_id = Column(Integer, primary_key=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey('author.author_id'))
    paper_id = Column(Integer, ForeignKey('paper.paper_id'))
    author = relationship("Author", back_populates='authorship')
    paper = relationship("Paper", back_populates='authorship')
    