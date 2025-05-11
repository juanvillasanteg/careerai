import os

from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

DATA_DIR = os.getenv("DATA_DIR", "data/")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
# QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "careerai-resume")


def load_and_persist_documents(
    data_dir: str = DATA_DIR,
    qdrant_url: str | None = QDRANT_URL,
    qdrant_api_key: str | None = QDRANT_API_KEY,
    # qdrant_collection: str = QDRANT_COLLECTION,
) -> VectorStoreIndex:
    """Load documents from a directory, vectorize, and persist to Qdrant.

    Args:
        data_dir (str): Path to the directory containing documents.
        qdrant_url (Optional[str]): Qdrant Cloud URL.
        qdrant_api_key (Optional[str]): Qdrant Cloud API key.
        qdrant_collection (str): Name of the Qdrant collection.

    Returns:
        VectorStoreIndex: The index object for querying.

    """
    # Load documents
    documents = SimpleDirectoryReader(data_dir).load_data()

    # Connect to Qdrant Cloud
    client = QdrantClient(
        url=qdrant_url,
        api_key=qdrant_api_key,
    )

    # Set up Qdrant vector store
    vector_store = QdrantVectorStore(
        client=client,
        collection_name="careerai-resume",
    )

    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Create and persist index
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        # vector_store=vector_store,
        show_progress=True,
    )
    return index
