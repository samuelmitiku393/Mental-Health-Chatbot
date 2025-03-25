from fastapi import APIRouter
from app.models.chat import Message

router = APIRouter()

# A simple endpoint to send a message
@router.post("/send_message/")
async def send_message(message: Message):
    return {"message": f"Message received: {message.content}"}

# An endpoint to get the list of messages (example)
@router.get("/messages/")
async def get_messages():
    return [{"sender": "John", "content": "Hello, World!"}]
