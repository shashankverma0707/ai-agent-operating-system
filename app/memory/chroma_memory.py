import chromadb
from app.config.settings import CHROMA_COLLECTION

client = chromadb.Client()
collection = client.get_or_create_collection(CHROMA_COLLECTION)


def store_memory(memory_id: str, content: str):
    collection.add(
        documents=[content],
        ids=[memory_id]
    )


def search_memory(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    return results