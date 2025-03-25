import sys
from pathlib import Path
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Set up the backend FastAPI app
app = FastAPI()

# Allow frontend to access the backend (CORS)
origins = [
    "http://localhost:3000",  # Add your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],
)

# Create a route to check if the backend is running
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

# Define the Message model for the chatbot
class Message(BaseModel):
    message: str

# Chatbot route to handle user messages
@app.post("/chatbot")
async def chatbot(message: Message):
    user_message = message.message.lower()
    if "hello" in user_message:
        reply = "Hi! How can I help you today?"
    else:
        reply = "I'm here to listen. Tell me more."
    return {"reply": reply}
