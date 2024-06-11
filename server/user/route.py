from fastapi import APIRouter, HTTPException
from .session import create_user
from .schema import UserSerializer


auth = APIRouter()

@auth.post("/new-user")
async def user(serializer: UserSerializer):
    await create_user(serializer.username, serializer.email, serializer.password)
    return  HTTPException(status_code=201, detail="User created")