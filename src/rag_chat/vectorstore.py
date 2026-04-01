from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from rag_chat import settings
from rag_chat.logger import get_logger

log = get_logger(__name__)

INDEX_PATH = Path(".faiss_index")


def _embeddings():
    return OpenAIEmbeddings(api_key=settings.openai_api_key)


def build_index(chunks: list[Document]) -> FAISS:
    log.info("Building FAISS index...")
    store = FAISS.from_documents(chunks, _embeddings())
    store.save_local(str(INDEX_PATH))
    log.info(f"Index saved → {INDEX_PATH}")
    return store


def load_index() -> FAISS | None:
    if INDEX_PATH.exists():
        log.info("Loading existing FAISS index")
        return FAISS.load_local(str(INDEX_PATH), _embeddings(),
                                allow_dangerous_deserialization=True)
    return None


def get_or_build_index(chunks: list[Document]) -> FAISS:
    return load_index() or build_index(chunks)