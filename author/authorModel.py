import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from core.db import Base

class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    affiliation_1 = Column(String(100), nullable=True)
    affiliation_2 = Column(String(100), nullable=True)
    email = Column(String(60), nullable=True)
    createdat = Column(DateTime, default=datetime.datetime.now())
    authorship = relationship("Authorship", back_populates='author')
