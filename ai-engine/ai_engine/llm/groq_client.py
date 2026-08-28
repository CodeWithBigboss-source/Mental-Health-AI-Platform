from groq import Groq
from ai_engine.core.config import settings

client = Groq(api_key=settings.groq_api_key)

def generate(messages: list[dict], model: str = None, temperature: float = None) -> str:
    """
    messages: list of {"role": "system"|"user"|"assistant", "content": str}
    """
    response = client.chat.completions.create(
        model=model or settings.model_name,
        messages=messages,
        temperature=temperature if temperature is not None else settings.temperature,
        max_tokens=settings.max_tokens,
    )
    return response.choices[0].message.content
