from .chroma_client import chroma_client

store_chunks = chroma_client.store_chunks
query_chunks = chroma_client.query_chunks

__all__ = [
    "store_chunks",
    "query_chunks"
]