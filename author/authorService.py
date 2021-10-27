from author.authorDTO import AuthorCreate
from author.authorModel import Author
from sqlalchemy.orm import Session


def create_author(author: AuthorCreate, db: Session):
    db_author = Author(first_name=author.first_name, middle_name=author.middle_name, last_name=author.last_name,
                       affiliation_1=author.affiliation_1, affiliation_2=author.affiliation_2, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(author_id: int, db: Session):
    return db.query(Author).filter(Author.author_id == author_id).first()


def get_authors(db: Session):
    return db.query(Author).all()
