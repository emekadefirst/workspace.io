from pydantic import BaseModel

class RoomSerializer(BaseModel):
    room_name: str