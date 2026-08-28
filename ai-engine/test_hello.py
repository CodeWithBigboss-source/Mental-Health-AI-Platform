from ai_engine.llm.groq_client import generate
from ai_engine.prompts.base_prompt import build_system_prompt

messages = [
    {"role": "system", "content": build_system_prompt()},
    {"role": "user", "content": "I've been really stressed about work lately."},
]

print(generate(messages))
