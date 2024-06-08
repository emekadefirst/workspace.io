from fastapi import FastAPI, WebSocket, HTTPException, WebSocketDisconnect
from sessions import add_message, create_user, fetch_messages_from_db

from fastapi.middleware.cors import CORSMiddleware
from serializiers import UserSerializer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/message")
def get_messages():
    messages = fetch_messages_from_db()
    if not messages:
        return {"message": "No results"}
    return messages

@app.post("/new-user")
async def user(serializer: UserSerializer):
    create_user(serializer.username, serializer.email, serializer.password)
    return  HTTPException(status_code=201, detail="User created")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data_in = await websocket.receive_text()
            # Add message to database or storage
            add_message(data_in)
            # Send back the received message
            await websocket.send_text(f"Message text was: {data_in}")
    except WebSocketDisconnect:
        return "WebSocket disconnected"
        
        
    