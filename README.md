# RAG App – Retrieval-Augmented Generation with FastAPI, ChromaDB & Gemini

A minimal, modular backend application that performs **semantic search** over documents using a Retrieval-Augmented Generation (RAG) pipeline powered by:

- **FastAPI** (backend API)
- **ChromaDB** (vector database)
- **SentenceTransformers** (embeddings)
- **Gemini 2.0 Flash** (LLM for answering queries)

---

# Features

- Upload PDF documents via API
- Extract and chunk document text
- Embed chunks using `SentenceTransformers`
- Store and search using ChromaDB
- Ask questions, get answers from Gemini (RAG-style)

---

# Tech Stack

| Layer       | Tool                         |
|-------------|------------------------------|
| Framework   | FastAPI                      |
| LLM         | Gemini 2.0 Flash             |
| Embeddings  | SentenceTransformers         |
| Vector DB   | ChromaDB                     |
| OCR/Text    | PyMuPDF                      |

---

# Project Structure

rag-app/
│
├── app/
│ ├── main.py 
│ ├── config.py   
│ │
│ ├── routers/ 
│ │ ├── upload.py 
│ │ ├── query.py 
│ │
│ ├── services/ 
│ │ ├── file_loader.py 
│ │ ├── chunker.py 
│ │ ├── embedder.py 
│ │ ├── retriever.py 
│ │ ├── generator.py 
│ │
│ ├── db/
│ │ ├── chroma_client.py 
│
├── data/
│ ├── uploads/ 
│ ├── processed/ # (Optional) 
│
├── requirements.txt 
├── .env # Environment variables
└── README.md 

---

# ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-app.git
cd rag-app

pip install -r requirements.txt

```

# Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key_here
MODEL_NAME=all-MiniLM-L6-v2
CHROMA_COLLECTION=rag_collection

# Run the App

```bash
uvicorn app.main:app --reload
```

