from sqlmodel import SQLModel, Session, create_engine

from .config import DATABASE_URL, DB_TIMEZONE

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL needs to be set")

engine = create_engine(DATABASE_URL)

def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)
    print("database tables created")

def get_session():
    with Session(engine) as session:
        yield session
