# app/routers/__init__.py
"""
API Routers Package
Contains all FastAPI router modules for different endpoints.
"""

from .upload import router as upload_router
from .query import router as query_router

__all__ = [
    "upload_router",
    "query_router",
]