from pydantic import BaseModel

class UserSerializer(BaseModel):
    username: str
    email: str
    password: str