from fastapi import APIRouter, Depends
from author.authorshipService import add_authorship, get_by_author, get_by_paper
from author.authorshipDTO import AuthorshipCreate
from core.connect import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/authorship/add")
def add_as(authship: AuthorshipCreate, db: Session = Depends(get_db)):
    return add_authorship(db=db, authorship=authship)


@router.get("/authorship/author/{author_id}")
def get_byauthor(author_id: int, db: Session = Depends(get_db)):
    return get_by_author(author_id=author_id, db=db)


@router.get("/authorship/paper/{paper_id}")
def get_bypaper(paper_id: int, db: Session = Depends(get_db)):
    return get_by_paper(paper_id=paper_id, db=db)
