"""
RAG Application Package
Main package for the Retrieval-Augmented Generation system.
"""

__version__ = "1.0.0"
__author__ = "Karthick Roshan"
__description__ = "RAG Backend API using FastAPI + ChromaDB + Gemini"

from .main import app

__all__ = ["app"]