import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma  # Using Chroma, not FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_nexus_response(user_query):
    # 1. Setup Embeddings (Must match ingest.py)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Load the Chroma DB we just created
    vector_db = Chroma(
        persist_directory="./chroma_db", 
        embedding_function=embeddings
    )
    
    # 3. Setup Retriever and LLM
    # 3. Setup Retriever and LLM
    retriever = vector_db.as_retriever(search_kwargs={"k": 4})
    llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile")

    # 4. Define the Prompt Template (Requirement 3: Guardrails)
    template = """Answer the question based ONLY on the following context:
    {context}

    Question: {question}
    
    If the answer is not in the context, strictly say: 'I am sorry, but I can only answer questions based on the company policy documents provided.'
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 5. Build the Chain
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # 6. Execute and Return (Requirement 6: Citations)
    answer = chain.invoke(user_query)
    docs = retriever.invoke(user_query)
    
    return answer, docs