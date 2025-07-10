# app/routers/upload.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil

from app.config import UPLOAD_DIR
from app.services.file_loader import extract_text_from_pdf
from app.services.chunker import chunk_text
from app.services import embed_chunks
from app.db.chroma_client import chroma_client

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """Upload and process PDF file."""
    try:
        # Save uploaded file
        filename = file.filename
        file_path = os.path.join(UPLOAD_DIR, filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        

        # Extract text from PDF
        text = extract_text_from_pdf(file_path)
        
        if not text.strip():
            raise HTTPException(status_code=400, detail="No text extracted from PDF")
        
        # Chunk text
        chunks = chunk_text(text)
        
        # Generate embeddings
        embedded_chunks = embed_chunks(chunks)
        
        # Store in ChromaDB
        chroma_client.store_chunks(embedded_chunks, chunks, metadata={"source": filename})
        
        return {
            "message": "File uploaded and processed successfully",
            "filename": filename,
            "chunks_count": len(chunks)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))