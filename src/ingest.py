import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def ingest_docs():
    documents = []
    # Ensure this points to your 'data' folder
    for file in os.listdir('./data'):
        if file.endswith('.md'):
            loader = TextLoader(os.path.join('./data', file), encoding='utf-8')
            documents.extend(loader.load())

    # chunk_size=1000 ensures the full policy sentence stays together
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create the fresh chroma_db folder
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    print(f"✅ Success! Ingested {len(chunks)} chunks into Chroma DB.")

if __name__ == "__main__":
    ingest_docs()