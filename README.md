# rag-chat-pro

![Python](https://img.shields.io/badge/python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

> A production-grade RAG (Retrieval Augmented Generation) chatbot that lets you chat with your PDF documents. Supports OpenAI, Anthropic, Groq, and Ollama — swap providers with a single `.env` change.

## Architecture

```
PDF/TXT files → Text chunks → FAISS vector index → RAG chain → Streamlit UI
                                                         ↑
                                          Switchable AI provider
                               (OpenAI · Anthropic · Groq · Ollama)
```

## Features

- Chat with any PDF or TXT document
- FAISS vector store with persistence across sessions
- Switchable AI provider — OpenAI, Anthropic, Groq, or Ollama
- Conversation memory across turns
- Source document display for every answer
- Fully local mode via Ollama (no API key needed)

## Quick start

### 1. Clone and set up environment

```bash
git clone https://github.com/wahhabriaz/rag-chat-pro
cd rag-chat-pro
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -e .
```

### 2. Set up `.env`

```bash
cp .env.example .env
```

### 3. Run locally free with Ollama

Install Ollama from https://ollama.com/download then:

```bash
ollama pull llama3.2
```

Set your `.env`:

```env
RAG_PROVIDER=ollama
RAG_MODEL=llama3.2
RAG_OLLAMA_BASE_URL=http://localhost:11434
RAG_DOCS_DIR=./docs
```

### 4. Add your documents

Drop any PDF or TXT files into the `docs/` folder.

### 5. Run the app

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Switching AI providers

Change `RAG_PROVIDER` in `.env`:

| Provider       | Value       | Model example             | API key needed  |
| -------------- | ----------- | ------------------------- | --------------- |
| Ollama (local) | `ollama`    | `llama3.2`                | No              |
| OpenAI         | `openai`    | `gpt-4o-mini`             | Yes             |
| Anthropic      | `anthropic` | `claude-3-haiku-20240307` | Yes             |
| Groq (free)    | `groq`      | `llama3-8b-8192`          | Yes (free tier) |

## Environment variables

| Variable                | Default                  | Description                  |
| ----------------------- | ------------------------ | ---------------------------- |
| `RAG_PROVIDER`          | `openai`                 | AI provider to use           |
| `RAG_MODEL`             | `gpt-4o-mini`            | Model name                   |
| `RAG_DOCS_DIR`          | `./docs`                 | Folder containing PDFs       |
| `RAG_CHUNK_SIZE`        | `500`                    | Text chunk size in chars     |
| `RAG_CHUNK_OVERLAP`     | `50`                     | Overlap between chunks       |
| `RAG_TOP_K`             | `4`                      | Number of chunks to retrieve |
| `RAG_OPENAI_API_KEY`    | —                        | OpenAI API key               |
| `RAG_ANTHROPIC_API_KEY` | —                        | Anthropic API key            |
| `RAG_GROQ_API_KEY`      | —                        | Groq API key                 |
| `RAG_OLLAMA_BASE_URL`   | `http://localhost:11434` | Ollama server URL            |

## Project structure

```
rag-chat-pro/
├── src/rag_chat/
│   ├── __init__.py       # Settings
│   ├── providers.py      # Switchable AI providers
│   ├── loader.py         # PDF + text ingestion
│   ├── vectorstore.py    # FAISS index
│   ├── chain.py          # RAG chain with memory
│   └── logger.py
├── app.py                # Streamlit UI
├── docs/                 # Drop PDFs here
└── .env.example
```

## Tech stack

Python 3.11 · LangChain · FAISS · Streamlit · OpenAI · Anthropic · Groq · Ollama · PyPDF
