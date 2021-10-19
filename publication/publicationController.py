from fastapi import APIRouter, HTTPException, Depends
from publication.publicationService import create_publicationtype
from publication.publicationDTO import PublicationCreate
from core.connect import get_db
from sqlalchemy.orm import Session

router = APIRouter()
@router.post("/publications")
async def create_pubtype(pub: PublicationCreate, db: Session = Depends(get_db)):
    return await create_publicationtype(pub=pub,db=db)
