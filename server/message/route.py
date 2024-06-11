from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .session import add_message, fetch_messages_from_db

message = APIRouter()


@message.get("/message")
def get_messages():
    messages = fetch_messages_from_db()
    if not messages:
        return {"message": "No results"}
    return messages


@message.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data_in = await websocket.receive_text()
            add_message(data_in)

            await websocket.send_text(f"Message text was: {data_in}")
    except WebSocketDisconnect:
        return "WebSocket disconnected"
        
