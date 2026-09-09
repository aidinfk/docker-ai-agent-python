import os
import sqlmodel
from sqlmodel import Session, SQLModel


DATABASE_URL = os.environ.get("DATABASE_URL") 

if DATABASE_URL == "":
    raise NotImplementedError("`DATABASE_URL` needs to be set.")


engine = sqlmodel.create_engine(DATABASE_URL)

# database models
# does not create db migrations
def init_db():
    print("createing database tables...")
    SQLModel.metadata.create_all(engine)

# api route
def get_session():
    with Session(engine) as session:
        yield session
