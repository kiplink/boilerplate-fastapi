from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from env import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT

db_conn_string = 'postgresql://%s:%s@%s:%s/%s' % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)
engine = create_engine(
    db_conn_string, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
