from fastapi import APIRouter, Depends
from author.authorService import create_author, get_author, get_authors
from author.authorDTO import AuthorCreate
from core.connect import get_db
from sqlalchemy.orm import Session


router = APIRouter()
@router.post("/author/add")
def add_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(author=author, db=db)


@router.get("/author/{author_id}")
def getauthor(author_id: int, db: Session = Depends(get_db)):
    return get_author(author_id=author_id, db=db)


@router.get("/authors")
def getauthors(db: Session = Depends(get_db)):
    return get_authors(db=db)
