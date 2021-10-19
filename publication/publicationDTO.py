from pydantic import BaseModel


class PublicationBase(BaseModel):
    publication_type: str


class PublicationCreate(PublicationBase):
    publication_type: str


class Publication(PublicationBase):
    id: int
    publication_type: str

    class Config:
        orm_mode = True
