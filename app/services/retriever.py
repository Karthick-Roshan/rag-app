# app/services/retriever.py
from app.db.chroma_client import chroma_client
from app.services import embedding_service
from app.config import TOP_K

class RetrievalService:
    def __init__(self):
        self.chroma_client = chroma_client
        self.embedding_service = embedding_service
    
    def retrieve_context(self, query: str, top_k: int = TOP_K) -> list[str]:
        """Retrieve relevant context chunks for a query."""
        query_embedding = self.embedding_service.embed_chunks([query])[0]
        
        context_chunks = self.chroma_client.query_chunks(query_embedding, top_k)
        
        return context_chunks

retrieval_service = RetrievalService()