import uuid

from pydantic import BaseModel


class AuthorshipBase(BaseModel):
    paper_id: uuid.UUID
    author_id: int


class AuthorshipCreate(AuthorshipBase):
    paper_id: uuid.UUID
    author_id: int


class Authorship(AuthorshipBase):
    authorship_id: int
    paper_id: uuid.UUID
    author_id: int

    class Config:
        orm_mode = True
