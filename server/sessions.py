from database import engine
from sqlmodel import Session, select
from models import User, Message

"""Message session manager"""
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

"""User session manager"""    
def create_user(username, email, password):
    with Session(engine) as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()
        return "User created Successfully"
    
def get_all_user():
    with Session(engine) as session:
        users = session.exec(User).all()
        return users
    
def get_by_id():
    with Session(engine) as session:
        user = session.exec(User).filter(User, id).all()
        return user
    

def delete_user():
    with Session(engine) as session:
        user = session.exec(User).filter(User, id).all()
        session.delete(user)
        session.commit()
        return f"{user} deleted successfully"
        
