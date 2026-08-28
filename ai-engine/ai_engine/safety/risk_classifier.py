import json
from ai_engine.llm.groq_client import generate

CRISIS_KEYWORDS = [
    "kill myself", "end my life", "suicide", "want to die", "not want to be alive",
    "hurt myself", "self harm", "self-harm", "cutting myself", "overdose",
    "no reason to live", "better off dead",
]

CLASSIFIER_PROMPT = """You are a safety classifier for a mental-health support app.
Classify the risk level of the user's message into exactly one of:
0 = general conversation, no distress
1 = mild distress (stress, sadness, normal worry)
2 = moderate concern (persistent low mood, anxiety symptoms, sleep problems)
3 = high concern (severe distress, panic, hopelessness, possible depression symptoms)
4 = immediate safety risk (self-harm, suicidal ideation, harm to others, danger)

Respond ONLY with valid JSON, no other text:
{{"risk_level": <int>, "reason": "<short reason>"}}

User message: "{message}"
"""

def classify_risk(message: str) -> dict:
    lowered = message.lower()
    for kw in CRISIS_KEYWORDS:
        if kw in lowered:
            return {"risk_level": 4, "reason": f"crisis keyword match: '{kw}'"}

    prompt = CLASSIFIER_PROMPT.format(message=message)
    raw = generate(
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    try:
        result = json.loads(raw.strip())
        result["risk_level"] = int(result["risk_level"])
        return result
    except (json.JSONDecodeError, KeyError, ValueError):
        # fail safe: if we can't parse it, treat as moderate concern rather than 0
        return {"risk_level": 2, "reason": "classifier parse failure, defaulting to moderate"}
