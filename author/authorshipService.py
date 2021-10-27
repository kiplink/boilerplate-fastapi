from author.authorshipDTO import AuthorshipCreate
from author.authorshipModel import Authorship
from sqlalchemy.orm import Session


def add_authorship(db: Session, authorship: AuthorshipCreate):
    que = Authorship(paper_id=authorship.paper_id, author_id=authorship.author_id)
    db.add(que)
    db.commit()
    db.refresh(que)
    return que


def get_by_author(author_id: int, db: Session):
    return db.query(Authorship).filter(Authorship.author_id == author_id).all()


def get_by_paper(paper_id: int, db: Session):
    return db.query(Authorship).filter(Authorship.paper_id == paper_id).all()
