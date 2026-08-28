from ai_engine.memory.conversation_memory import ConversationMemory
from ai_engine.core.orchestrator import handle_message

memory = ConversationMemory()

test_messages = [
    "I've been really stressed about work lately.",
    "I can't sleep and I keep overthinking everything.",
]

for msg in test_messages:
    print(f"\nUSER: {msg}")
    result = handle_message(memory, msg)
    print(f"[risk={result['risk_level']} action={result['safety_action']}]")
    print(f"AI: {result['response']}")
