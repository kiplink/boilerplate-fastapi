from fastapi import APIRouter, Depends
from publication.publicationService import create_publicationtype, get_pub, get_pubs
from publication.publicationDTO import PublicationCreate
from core.connect import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/publications")
async def create_pubtype(pub: PublicationCreate, db: Session = Depends(get_db)):
    return await create_publicationtype(pub=pub, db=db)


@router.get("/publication/{id}")
def get_publication(id: int, db: Session = Depends(get_db)):
    return get_pub(id=id, db=db)


@router.get("/publications")
def get_publications(db: Session = Depends(get_db)):
    return get_pubs(db=db)
