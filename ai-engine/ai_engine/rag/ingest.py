from supabase import create_client
from ai_engine.core.config import settings
from ai_engine.rag.embeddings import embed

supabase = create_client(settings.supabase_url, settings.supabase_key)

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def ingest_document(text: str, metadata: dict):
    chunks = chunk_text(text)
    rows = [
        {"content": chunk, "metadata": metadata, "embedding": embed(chunk)}
        for chunk in chunks
    ]
    supabase.table("documents").insert(rows).execute()
    print(f"Ingested {len(rows)} chunks with metadata {metadata}")
