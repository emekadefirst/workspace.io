from models import User
from sqlmodel import Session
from .database import engine

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
        
