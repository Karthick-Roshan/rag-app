# app/config.py

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Gemini API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Embedding model name
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")

# Chroma collection name
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "rag_collection")

# Upload folder path
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "uploads")  
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")

# Chunking settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "300"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))

# Retrieval settings
TOP_K = int(os.getenv("TOP_K", "5")) 
