from models import Room
from sqlmodel import Session
from sqlmodel import select
from .database import engine

def create_room(room):
    with Session(engine) as session:
        session.add(Room(room=room))
        session.commit()
        return "Room successfully created"

def get_room(id):
    with Session(engine) as session:
        return session.get(Room, id)

def get_rooms():
    with Session(engine) as session:
        statement = select(Room).offset().limit()
        results = session.exec(statement)
        return results.all()

def update_room(int, room_data: Room):
    with Session(engine) as session:
        room = session.get(Room, int)
        if room:
            for key, value in room_data.dict(exclude_unset=True).items():
                setattr(room, key, value)
            session.add(room)
            session.commit()
            session.refresh(room)
            return room
        return None

def delete_room(id):
    with Session(engine) as session:
        room = session.get(Room, id)
        if room:
            session.delete(room)
            session.commit()
            return True
        return False
