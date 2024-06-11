from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from message.route import message
from user.route import auth
from newsletter.route import nwl
from sqlmodel import SQLModel, create_engine
from models import *

db_name = "message.db"
db_url = f"sqlite:///{db_name}"
engine = create_engine(db_url, echo=True)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def run_db():
    Message, User, NewsLetter, Room
    create_db_and_table()

app = FastAPI()

def main():
    run_db()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(message)
    app.include_router(auth)
    app.include_router(nwl)



main()




        
        
    