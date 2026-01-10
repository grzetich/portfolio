from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

from rag_service import RAGService

load_dotenv()

app = FastAPI(title="Resume RAG Chatbot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_service = RAGService()

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = None

@app.on_event("startup")
async def startup_event():
    await rag_service.initialize()

@app.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    try:
        response = await rag_service.query(message.message)
        return ChatResponse(
            response=response["answer"],
            sources=response.get("sources", [])
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/ingest")
async def ingest_resume():
    try:
        result = await rag_service.ingest_resume()
        return {"message": "Resume ingested successfully", "chunks": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)