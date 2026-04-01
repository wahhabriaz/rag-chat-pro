from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from rag_chat import settings
from rag_chat.logger import get_logger

log = get_logger(__name__)


def load_documents(path: str | Path | None = None) -> list[Document]:
    src = Path(path or settings.docs_dir)
    docs: list[Document] = []

    files = list(src.glob("*.pdf")) + list(src.glob("*.txt"))
    if not files:
        raise FileNotFoundError(f"No PDF or TXT files found in {src}")

    for f in files:
        try:
            loader = PyPDFLoader(str(f)) if f.suffix == ".pdf" else TextLoader(str(f))
            docs.extend(loader.load())
            log.info(f"Loaded {f.name}")
        except Exception as exc:
            log.warning(f"Skipping {f.name}: {exc}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    chunks = splitter.split_documents(docs)
    log.info(f"Split into {len(chunks)} chunks")
    return chunks