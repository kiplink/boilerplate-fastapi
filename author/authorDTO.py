from pydantic import BaseModel
from typing import Optional


class AuthorBase(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    affiliation_1: Optional[str] = None
    affiliation_2: Optional[str] = None
    email: Optional[str] = None


class AuthorCreate(AuthorBase):
    first_name: str


class Author(AuthorBase):
    author_id: int
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    affiliation_1: Optional[str] = None
    affiliation_2: Optional[str] = None
    email: str

    class Config:
        orm_mode = True
