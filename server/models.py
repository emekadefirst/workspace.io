from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
 
class User(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str    
    messages: List["Message"] = Relationship(back_populates="user")
    rooms: List["Room"] = Relationship(back_populates="user")
    
class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str 
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="messages")
    created_at: datetime = Field(default=datetime.utcnow)

class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(default=None, max_length=50)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="rooms")

class NewsLetter(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    email: str = Field(default=None, unique=True)
