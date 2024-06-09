from sqlmodel import SQLModel, Field
from database import create_db_and_table
 
class User(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str    
    
class Message(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    message: str 
    # user: str = Field(default=None, foreign_key="user.username")

create_db_and_table()