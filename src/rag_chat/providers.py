from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from langchain.schema.language_model import BaseLanguageModel
from rag_chat import settings


def get_llm() -> BaseLanguageModel:
    p = settings.provider.lower()
    if p == "openai":
        return ChatOpenAI(
            model=settings.model,
            api_key=settings.openai_api_key,
            temperature=0.2,
        )
    elif p == "anthropic":
        return ChatAnthropic(
            model=settings.model or "claude-3-haiku-20240307",
            api_key=settings.anthropic_api_key,
            temperature=0.2,
        )
    elif p == "groq":
        return ChatGroq(
            model=settings.model or "llama3-8b-8192",
            api_key=settings.groq_api_key,
            temperature=0.2,
        )
    elif p == "ollama":
        return Ollama(
            model=settings.model or "llama3",
            base_url=settings.ollama_base_url,
        )
    else:
        raise ValueError(f"Unknown provider: {p}. Use openai/anthropic/groq/ollama")