# api.py
from fastapi import APIRouter, HTTPException
from .session import create_room, get_room, get_rooms, update_room, delete_room
from .schema import RoomSerializer

room = APIRouter()

@room.post("/room/create")
async def create(room: RoomSerializer):
    db_room = await create_room(room.dict())
    return db_room

@room.get("/room/{id}")
async def read_room(id):
    db_room = await get_room(id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@room.get("/rooms")
async def read_rooms():
    return await get_rooms()

@room.put("/room/{id}")
async def update(id):
    updated_room = await update_room(id)
    if updated_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return updated_room

@room.delete("/room/{id}")
async def delete(id):
    if not await delete_room(id):
        raise HTTPException(status_code=404, detail="Room not found")
    return {"message": "Room deleted successfully"}
