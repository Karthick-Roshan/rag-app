# app/chunker.py

def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list:
    """
    Splits text into overlapping chunks.
    Each chunk has 'chunk_size' words, overlapping 'overlap' words.
    """
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        if end == len(words):
            break

        start += chunk_size - overlap

    return chunks
