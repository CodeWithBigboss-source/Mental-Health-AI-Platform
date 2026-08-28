from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    groq_api_key: str
    supabase_url: str
    supabase_key: str
    model_name: str = "openai/gpt-oss-120b"
    max_tokens: int = 1024
    temperature: float = 0.7

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
