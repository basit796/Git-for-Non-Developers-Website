"""
FastAPI server for Git Book Agent
Provides REST API endpoints for the chatbot frontend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from agent import create_agent

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Git Book Agent API",
    description="RAG-powered agent for Git learning book",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent globally
agent = None


@app.on_event("startup")
async def startup_event():
    """Initialize agent on startup"""
    global agent
    print("🚀 Starting Git Book Agent API...")
    try:
        agent = create_agent()
        print("✅ Agent initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    conversation_id: Optional[str] = None


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "service": "Git Book Agent API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    embeddings_exist = os.path.exists('embeddings.npy')
    metadata_exists = os.path.exists('metadata.json')
    
    return {
        "status": "healthy" if (embeddings_exist and metadata_exists and agent) else "unhealthy",
        "agent_initialized": agent is not None,
        "embeddings_ready": embeddings_exist,
        "metadata_ready": metadata_exists
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint for user questions.
    
    Args:
        request (ChatRequest): User message
        
    Returns:
        ChatResponse: Agent response
    """
    if not agent:
        raise HTTPException(status_code=503, detail="Agent not initialized")
    
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    try:
        # Get response from agent
        response = agent.chat(request.message)
        
        return ChatResponse(
            response=response,
            conversation_id=request.conversation_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")


@app.get("/chapters")
async def get_chapters():
    """Get list of book chapters"""
    from tools import get_chapter_list
    return {"chapters": get_chapter_list()}


if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    
    print(f"\n{'='*80}")
    print(f"🚀 Starting Git Book Agent API Server")
    print(f"{'='*80}")
    print(f"📡 Server will run on: http://0.0.0.0:{port}")
    print(f"📚 API docs available at: http://localhost:{port}/docs")
    print(f"{'='*80}\n")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
