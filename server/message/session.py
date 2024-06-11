from sqlmodel import Session, select
from .database import engine
from models import Message

def add_message(message):
    with Session(engine) as session:
        session.add(Message(message=message))
        session.commit()
        return "Message added Successfully"
    

def fetch_messages_from_db():
    with Session(engine) as session:
        statement = select(Message)
        results = session.exec(statement).all()
        return results
    
def get_by_id():
    with Session(engine) as session:
        messages = session.exec(Message).filter(Message, id).all()
        return messages
    
def delete_messages(messages):
    with Session(engine) as session:
        session.delete(messages)
        session.commit()
        return "Message deleted Successfully"
    
def update_message(message):
    with Session(engine) as session:
        messages = session.exec(Message).filter(Message, id).all()
        messages[0].message = message
        session.commit()
        return "Message updated Successfully"
