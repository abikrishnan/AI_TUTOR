from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

# Simulating Azure response
# Replace this with actual Azure SDK code

class QuestionRequest(BaseModel):
    chapter: str
    section: str
    question: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_ai(data: QuestionRequest):
    response = {
        "answer": f"(Mock) AI Response to: '{data.question}' in {data.chapter} - {data.section}."
    }
    return response