import json
import datetime
import uuid
from paper.paperDTO import PaperCreate
from paper.paperModel import Paper
from sqlalchemy.orm import Session
from core.elastic import es
from author.authorService import get_author
from author.authorshipService import add_authorship
from author.authorshipDTO import AuthorshipCreate


def add_paper(paper: PaperCreate, db: Session):
    try:
        data = {}
        names = []
        # save postgre
        id_ = uuid.uuid4()
        que = Paper(paper_id=id_,
                    publication_type=paper.publication_type,
                    title=paper.title,
                    abstract=paper.abstract,
                    doi=paper.doi,
                    publisher=paper.publisher,
                    publication_year=paper.publication_year)
        db.add(que)
        db.commit()
        db.refresh(que)
        # save to elastic
        for x in range(len(paper.author_id)):
            AuthorshipCreate.paper_id = id_
            AuthorshipCreate.author_id = paper.author_id[x]
            add_authorship(db=db, authorship=AuthorshipCreate)
            author_res = get_author(author_id=paper.author_id[x], db=db)
            name = author_res.first_name +" "+ (author_res.middle_name if author_res.middle_name else "")+" "+\
                   (author_res.last_name if author_res.last_name else "")
            names.append(name)
        print(id_)
        data["paper_id"] = str(id_)
        data["names"] = names
        data["title"] = paper.title
        data["abstract"] = paper.abstract
        data["publication_year"] = paper.publication_year
        data["doi"] = paper.doi
        data["publisher"] = paper.publisher
        y = json.dumps(data, default=convertjson)
        print(y)
        res = es.index(index="paper", document=y)
        print(res)
        return res
    except Exception as e:
        return str(e)


def convertjson(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
