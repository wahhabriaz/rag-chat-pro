from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from rag_chat.providers import get_llm
from rag_chat import settings


def build_chain(store: FAISS) -> ConversationalRetrievalChain:
    llm = get_llm()
    retriever = store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": settings.top_k},
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer",
    )
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        verbose=False,
    )