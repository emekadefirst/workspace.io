from models import NewsLetter
from .database import engine
from sqlmodel import Session

"""Newsletters session Manager"""
def add_email(email):
    with Session(engine) as session:
        session.add(NewsLetter(email=email))
        session.commit()
        return "email submited Successfully"
    
def remove_email():
    with Session(engine) as session:
        email = session.exec(NewsLetter).filter(NewsLetter, id).all()
        session.delete(email)
        session.commit()
        return f"{email} deleted successfully"