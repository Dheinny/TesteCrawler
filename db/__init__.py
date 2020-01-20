import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conn import Conn

engine = db.create_engine(
    Conn.get_url(),
    echo=True
)

meta = db.MetaData(engine)
Base = declarative_base(metadata=meta)

Session = sessionmaker()
Session.configure(bind=engine)
