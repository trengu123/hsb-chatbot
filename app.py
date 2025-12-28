from dotenv import load_dotenv
import os

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from bot import ask_bot

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],   # 👈 CỰC QUAN TRỌNG
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: list   # ✅ QUAN TRỌNG

@app.post("/chat")
def chat(req: ChatRequest):
    reply = ask_bot(req.messages)
    return {"reply": reply}

@app.get("/")
def root():
    return {"status": "OK"}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
