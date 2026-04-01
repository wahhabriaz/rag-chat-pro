from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="RAG_")
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    groq_api_key: str = ""
    ollama_base_url: str = "http://localhost:11434"
    docs_dir: str = "./docs"
    chunk_size: int = 500
    chunk_overlap: int = 50
    top_k: int = 4

settings = Settings()