# app/routers/query.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services import retrieve_context, generate_response

router = APIRouter(prefix="/query", tags=["query"])

class QueryRequest(BaseModel):
    query: str

@router.post("/")
async def query_rag(request: QueryRequest):
    """Process RAG query and return generated response."""
    try:
        context_chunks = retrieve_context(request.query)
        
        response = generate_response(context_chunks, request.query)
        
        return {
            "answer": response,
            "context_chunks_count": len(context_chunks)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))