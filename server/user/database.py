from sqlmodel import SQLModel, create_engine

db_name = "message.db"
db_url = f"sqlite:///{db_name}"
engine = create_engine(db_url, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)
        



