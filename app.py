import streamlit as st
from pathlib import Path
from rag_chat.loader import load_documents
from rag_chat.vectorstore import get_or_build_index
from rag_chat.chain import build_chain
from rag_chat import settings

st.set_page_config(page_title="RAG Chat Pro", page_icon="🤖", layout="wide")
st.title("RAG Chat Pro")
st.caption(f"Provider: `{settings.provider}` · Model: `{settings.model}`")

@st.cache_resource(show_spinner="Building knowledge base...")
def init_chain():
    chunks = load_documents()
    store = get_or_build_index(chunks)
    return build_chain(store)

chain = init_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = chain({"question": prompt})
            answer = result["answer"]
            sources = result.get("source_documents", [])

        st.markdown(answer)

        if sources:
            with st.expander("Sources"):
                for doc in sources[:3]:
                    st.caption(f"...{doc.page_content[:200]}...")

    st.session_state.messages.append({"role": "assistant", "content": answer})