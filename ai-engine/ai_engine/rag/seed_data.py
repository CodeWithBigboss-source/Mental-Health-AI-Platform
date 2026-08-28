from ai_engine.rag.ingest import ingest_document

DOCS = [
    {
        "text": "Box breathing is a simple technique to calm the nervous system. Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds, hold for 4 seconds. Repeat for 4-5 cycles. It is commonly used to reduce acute anxiety and panic symptoms by activating the parasympathetic nervous system.",
        "metadata": {"topic": "breathing", "source": "psychoeducation"},
    },
    {
        "text": "The 5-4-3-2-1 grounding technique helps during moments of overwhelm or dissociation. Identify 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste. This redirects attention to the present moment.",
        "metadata": {"topic": "grounding", "source": "psychoeducation"},
    },
    {
        "text": "Good sleep hygiene includes keeping a consistent sleep and wake time, avoiding screens 30-60 minutes before bed, keeping the bedroom cool and dark, and avoiding caffeine after early afternoon. Racing thoughts at bedtime can be addressed by writing worries down earlier in the evening rather than at bedtime.",
        "metadata": {"topic": "sleep", "source": "psychoeducation"},
    },
    {
        "text": "Cognitive reframing is a CBT technique where a person identifies an unhelpful automatic thought, examines the evidence for and against it, and constructs a more balanced alternative thought. For example, replacing 'I always fail' with 'I struggled with this one task, but I have succeeded at others before.'",
        "metadata": {"topic": "cbt", "source": "psychoeducation"},
    },
]

if __name__ == "__main__":
    for doc in DOCS:
        ingest_document(doc["text"], doc["metadata"])
