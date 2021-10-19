from publication.publicationDTO import PublicationCreate
from publication.publicationModel import PublicationType
from sqlalchemy.orm import Session


async def create_publicationtype(pub: PublicationCreate, db:Session):
  db_publication =  PublicationType(publication_type=pub.publication_type)
  db.add(db_publication)
  db.commit()
  db.refresh(db_publication)
  return db_publication