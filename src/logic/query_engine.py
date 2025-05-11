import os
from typing import Any

from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
# QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "careerai-resume")


def get_query_engine() -> RetrieverQueryEngine:
    """Set up and return a query engine for the Qdrant vector index.

    Returns:
        RetrieverQueryEngine: Configured query engine for retrieval.

    """
    # Connect to Qdrant Cloud
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )

    # Set up Qdrant vector store
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="careerai-resume",
    )

    # Create storage context and index
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_vector_store(
        vector_store,
        storage_context=storage_context,
    )

    # Set up query engine
    query_engine = index.as_query_engine()
    return query_engine


def query_resume(query: str) -> Any:
    """Query the resume vector index for relevant information.

    Args:
        query (str): The user's query string.

    Returns:
        Any: The response from the query engine.

    """
    engine = get_query_engine()
    response = engine.query(query)
    return response
