from sentence_transformers import SentenceTransformer
from app.config import MODEL_NAME

class EmbeddingModel:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)


    def embed_chunks(self, chunks: list[str]) -> list[list[float]]:
        """
        Accepts a list of text chunks and returns a list of vector embeddings.
        """
        embeddings = self.model.encode(chunks, show_progress_bar=True)
        return embeddings 
    
embedding_service = EmbeddingModel(MODEL_NAME)