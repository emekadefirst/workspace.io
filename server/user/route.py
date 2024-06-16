from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .session import create_user
from .schema import UserSerializer

auth = APIRouter()


@auth.post("/user/create", status_code=201)
async def create_new_user(serializer: UserSerializer):
    user = await create_user(serializer.username, serializer.email, serializer.password)
    return user


@auth.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


@auth.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Something went wrong"})
