from ai_engine.rag.ingest import supabase
from ai_engine.rag.embeddings import embed

def retrieve(query: str, top_k: int = 3, similarity_threshold: float = 0.3) -> list[dict]:
    query_embedding = embed(query)
    result = supabase.rpc(
        "match_documents",
        {"query_embedding": query_embedding, "match_count": top_k},
    ).execute()
    return [r for r in result.data if r["similarity"] >= similarity_threshold]
