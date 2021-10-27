from fastapi import APIRouter, Depends
from paper.paperService import add_paper
from paper.paperDTO import PaperCreate
from core.connect import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/paper/add")
def create_papers(paper: PaperCreate, db: Session = Depends(get_db)):
    return add_paper(paper=paper, db=db)
