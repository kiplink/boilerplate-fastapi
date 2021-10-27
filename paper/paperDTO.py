import uuid
from pydantic import BaseModel
from typing import Optional, List


class PaperBase(BaseModel):
    publication_type: int
    title: str
    abstract: str
    publication_year: int
    doi: str
    publisher: str


class PaperCreate(PaperBase):
    author_id: List[int]
    publication_type: int
    title: str
    abstract: Optional[str] = None
    publication_year: int
    doi: Optional[str] = None
    publisher: Optional[str] = None


class Paper(PaperBase):
    paper_id: uuid.UUID
    publication_type: int
    title: str
    abstract: str
    publication_year: int
    doi: str
    publication_year: str

    class Config:
        orm_mode = True

