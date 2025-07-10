import chromadb
from chromadb.config import Settings
from app.config import CHROMA_COLLECTION

class ChromaClient:
    def __init__(self):
        self.client = chromadb.Client(Settings(
            persist_directory="./chroma_storage",  
            anonymized_telemetry=False
        ))
        self.collection = self.client.get_or_create_collection(name=CHROMA_COLLECTION)
    
    def store_chunks(self, embeddings: list[list[float]], texts: list[str], metadata: dict = None):
        """Store embedded chunks in the ChromaDB collection."""
        ids = [f"chunk_{i}" for i in range(len(texts))]
        metadatas = [metadata or {} for _ in texts]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )

    def query_chunks(self, query_embedding: list[float], top_k: int = 5) -> list[str]:
        """Search ChromaDB using the query embedding and return top-k matching documents."""
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results["documents"][0]

chroma_client = ChromaClient()